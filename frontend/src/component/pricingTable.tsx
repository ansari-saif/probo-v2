

interface TableType {
    data: any,
    order_type: string
}

export const PriceTable = ({data, order_type}:TableType)=> {
  return (
    <table className="w-full mb-4 text-left">
      <thead>
        <tr>
          <th className="py-2 text-md font-semibold text-gray-700">PRICE</th>
          <th className="py-2 px-1 text-md font-light text-gray-700 text-right">
            QTY AT <span className={`${order_type === 'YES' ? 'text-[#1A7BFE]' : 'text-[#DB2706]'} `}>{order_type}</span>
          </th>
        </tr>
      </thead>
      <tbody>
        {data.map((row: any, index: number) => {
          let qut = row.quantity.toString();
          return <tr 
          style={{
            background: `linear-gradient(to left, ${order_type === 'YES' ? '#BBD8FE' : '#FFDCDB'} ${row.quantity !== 0 ? qut : 0}%, #ffffff ${0}%)`
          }}
           key={index} className={`border-t border-gray-200`}>
            <td className="py-2 px-2 text-sm text-gray-600">{row.price}</td>
            <td className="py-2 px-4 text-sm text-gray-600 text-right relative">
              
              <span className="relative z-10">{row.quantity}</span>
            </td>
          </tr>
})}
      </tbody>
    </table>
  );
}
