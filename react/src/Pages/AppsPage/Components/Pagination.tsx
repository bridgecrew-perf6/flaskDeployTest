import ReactPaginate from "react-paginate";
import 'bootstrap/dist/css/bootstrap.css';

interface PaginationProps{
    handlePageClick: (pageNumber: any) => void;
    numberOfPages: number;
}

export default function Pagination(props: PaginationProps){

    return(
        <ReactPaginate previousLabel={'Previous'}
                       nextLabel={'Next'}
                       breakLabel={'...'}
                       pageCount={props.numberOfPages}
                       marginPagesDisplayed={2}
                       pageRangeDisplayed={3}
                       onPageChange={props.handlePageClick}
                       containerClassName={'pagination justify-content-center'}
                       pageClassName={'page-item'}
                       pageLinkClassName={'page-link'}
                       previousClassName={'page-item'}
                       previousLinkClassName={'page-link'}
                       nextClassName={'page-item'}
                       nextLinkClassName={'page-link'}
                       breakClassName={'page-item'}
                       breakLinkClassName={'page-link'}
                       activeClassName={'active'}

        />
    )
}