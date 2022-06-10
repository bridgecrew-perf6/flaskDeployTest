import "mdb-react-ui-kit/dist/css/mdb.min.css";
import "../../CSS/footer.css";
export default function Footer() {
  return (
    <>
      <footer
        id="footer"
        className="bg-light fixed-bottom text-center text-lg-start"
      >
        <div
          className="text-center p-3" /*style="background-color: rgba(0, 0, 0, 0.2)"*/
        >
          © 2022 Copyright: Carmel Hecht, Lior Ushomirsky, Eliran Turgeman
        </div>
      </footer>
    </>
  );
}
