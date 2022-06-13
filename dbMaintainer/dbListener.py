
import pprint
from web3 import Web3
import asyncio
from threading import Thread
from contractInfo import dappstore_contract, app_created_filter, user_purchased_filter
import dbActions







# def handle_event(event):
#     print(Web3.toJSON(event))


# asynchronous defined function to loop
# this loop sets up an event filter and is looking for new entires for the "PairCreated" event
# this loop runs on a poll interval
# async def log_loop(event_filter, poll_interval):
#     while True:
#         # for event_data in event_filter.get_all_entries():
#         # # for event_data in event_filter.get_new_entries():
#         #     print("GOT SOMETHING")
#         #     print(Web3.toJSON(event_data))
#         # print("AAAAAAAAAA")
#         await asyncio.sleep(poll_interval)
        
        
async def purchases_listener():
    
    def extract_purchase_event_args(event_data):
        print("\n\n\n")
            
        event_data_args = event_data.args
        print(pprint.pp(event_data_args))
        
        print("App Creator: ", event_data_args.app_creator)
        print("App Purchaser: ", event_data_args.buyer)
        print("App Address: ", event_data_args.app_contract)
        
        print("\n\n\n")
        
        return {'app_addr': event_data_args.app_contract, 'creator_addr': event_data_args.app_creator, 'purchaser_addr': event_data_args.buyer}
            
    
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



if __name__ == "__main__":
    print("RUNNING dAppstore DB LISTENER")

    
    # insert_app_to_db(id=1, name="App 1", description="App 1 Description", category="App 1 Category")
    dbActions.get_filtered_app_ids(offset=0, length=10, textFilter="", categoryFilter="", ratingFilter=0)
    
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # try:
    #     loop.run_until_complete(
    #         asyncio.gather(
    #             # log_loop(app_created_filter, 1),
    #             purchases_listener(),
    #             )
    #         )
    # finally:
    #     # close loop to free up system resources
    #     print("Blockching Listener Task END")

    #     loop.close()
