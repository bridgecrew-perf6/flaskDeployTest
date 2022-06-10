import React from "react";
import "../../../CSS/PurchasedTable.css";
interface GlobalFilterProps {
  filter: string;
  setFilter: any;
}

export const GlobalFilter = ({ filter, setFilter }: GlobalFilterProps) => {
  return (
    <div className="global-filter">
      Search:{" "}
      <input value={filter || ""} onChange={(e) => setFilter(e.target.value)} />
    </div>
  );
};
