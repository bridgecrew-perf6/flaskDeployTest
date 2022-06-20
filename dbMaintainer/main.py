
import pprint
from web3 import Web3
import asyncio
from threading import Thread
from contractInfo import dappstore_contract, app_created_filter, user_purchased_filter, app_rated_filter, app_updated_filter
import dbActions


gathered_prev_creations=False

async def purchases_listener():
    
    def extract_purchase_event_args(event_data):
        print("\n\n\n")
            
        event_data_args = event_data.args
        print(pprint.pp(event_data_args))
        
        print("App Creator: ", event_data_args.app_creator)
        print("App Purchaser: ", event_data_args.buyer)
        print("App Address: ", event_data_args.app_contract)
        
        print("\n\n\n")
        
        return {
            'app_addr': event_data_args.app_contract,
            'creator_addr': event_data_args.app_creator,
            'purchaser_addr': event_data_args.buyer
            }
            
    while not gathered_prev_creations:
        await asyncio.sleep(1)
    
    prev_event_datas = user_purchased_filter.get_all_entries()
    print("Num of prev purchases events: " + str(len(prev_event_datas)))
    # Get all previous enteries
    
    for event_data in prev_event_datas:
        try:
            dbActions.add_purchase_do_db(**extract_purchase_event_args(event_data))
        except Exception as e:
            print("purchases_listener Exception: ", e)
    
    
    while True:
        try:
            for event_data in user_purchased_filter.get_new_entries():
                dbActions.add_purchase_do_db(**extract_purchase_event_args(event_data))
        except Exception as e:
            print("purchases_listener Exception: ", e)
            
        await asyncio.sleep(1)
        
async def rating_listener():
    def extract_rating_event_args(rating_event_data):
        event_data_args = rating_event_data.args

        app_id = event_data_args.app_id

        rating_int = event_data_args.rating_int
        rating_modulu = event_data_args.rating_modulu
        num_ratings = event_data_args.num_ratings
        
        rating = 0 if num_ratings == 0 else rating_int + (rating_modulu / num_ratings)
        
        
        print("\n\n\n")
        print(pprint.pp(event_data_args))
        print("App ID: ", id)
        print("App Rating: ", rating)
        print("\n\n\n")
        
        return {
            'app_id': app_id,
            'rating': rating
            }

    while not gathered_prev_creations:
        await asyncio.sleep(1)
        
    prev_event_datas = app_rated_filter.get_all_entries()
    print("Num of prev rating events: " + str(len(prev_event_datas)))
    
    # Get all previous enteries
    for event_data in prev_event_datas:
        try:
            dbActions.update_app_rating_db(**extract_rating_event_args(event_data))
        except Exception as e:
            print("rating_listener Exception: ", e)
    
    
    while True:
        try:
            for event_data in app_rated_filter.get_new_entries():
                print("GOT RATING EVENT")
                dbActions.update_app_rating_db(**extract_rating_event_args(event_data))
        except Exception as e:
            print("rating_listener Exception: ", e)
            
        await asyncio.sleep(1)



async def creation_listener():
    def extract_creation_event_args(event_data):
        print("\n\n\n")
            
        event_data_args = event_data.args
        print(pprint.pp(event_data_args))
        
        print("App Creator: ", event_data_args.creator)
        print("App Name: ", event_data_args.name)
        print("App Description: ", event_data_args.description)
        print("App Category: ", event_data_args.category)
        # print("App Rating: ", event_data_args.rating)
        # print("App Address: ", event_data_args.app_contract)
        
        print("\n\n\n")
        
        return {
                'id': event_data_args.id,
                'name': event_data_args.name,
                'description': event_data_args.description,
                'category': event_data_args.category,
                'rating': 0,
                # 'app_addr': event_data_args.app_contract
                }
        
        
    prev_event_datas = app_created_filter.get_all_entries()
    print("Num of prev creation events: " + str(len(prev_event_datas)))
    
    # Get all previous enteries
    for event_data in prev_event_datas:
        try:
            dbActions.insert_app_to_db(**extract_creation_event_args(event_data))
        except Exception as e:
            print("creation_listener Exception: ", e)
    global gathered_prev_creations
    gathered_prev_creations = True
    while True:
        try:
            for event_data in app_created_filter.get_new_entries():
                dbActions.insert_app_to_db(**extract_creation_event_args(event_data))
        except Exception as e:
            print("creation_listener Exception: ", e)
            
        await asyncio.sleep(1)

async def update_listener():
    async def extract_update_event_args(update_event_data):
        event_data_args = update_event_data.args
        app_id = event_data_args.app_id
        
        print(pprint.pp(event_data_args))
        print("Updated App ID: ", app_id)
        
        get_apps_res = dappstore_contract.functions.getAppBatch(app_id, 1).call()
        if len(get_apps_res) == 0:
            print("App not found")
            return None
        
        app_info = get_apps_res[0]
        app_name = app_info[1]
        app_description = app_info[2]
        print("Updated App Name: ", app_name)


        return {
            'app_id': app_id,
            'name': app_name,
            'description': app_description
            }

    while not gathered_prev_creations:
        await asyncio.sleep(1)
        
    prev_event_datas = app_updated_filter.get_all_entries()
    print("Num of prev update events: " + str(len(prev_event_datas)))
    print("Prev event datas: " + str(prev_event_datas))
    
    # Get all previous enteries
    for event_data in prev_event_datas:
        try:
            extracted_event_args = await extract_update_event_args(event_data)
            if extracted_event_args is not None:
                dbActions.update_app_name_description_db(**extracted_event_args)
        except Exception as e:
            print("update_listener Exception: ", e)
    
    
    while True:
        try:
            for event_data in app_updated_filter.get_new_entries():
                print("GOT Update EVENT")
                extracted_event_args = await extract_update_event_args(event_data)
                dbActions.update_app_name_description_db(**extracted_event_args)
        except Exception as e:
            print("update_listener Exception: ", e)
            
        await asyncio.sleep(1)

if __name__ == "__main__":
    print("RUNNING dAppstore DB LISTENER")

    # dbActions.insert_app_to_db(id=5, name="App 5 ", description="App 5 Description", category="ART", rating=5)
    # dbActions.get_filtered_app_ids(offset=0, length=10, textFilter="", categoryFilter="", ratingFilter=0)
    
    while True:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(
                asyncio.gather(
                    # log_loop(app_created_filter, 1),
                    #purchases_listener(),
                    creation_listener(),
                    rating_listener(),
                    update_listener()
                    )
                )
        finally:
            # close loop to free up system resources
            print("Blockching Listener Task END")
            loop.close()
