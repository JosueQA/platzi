import { createContext, useState } from "react";

export const ShoppingCartContext = createContext();

export function ShoppingCartProvider({ children }) {
  const [contador, setContador] = useState(0);

  const [isProductDetailOpen, setIsProductDetailOpen] = useState(false);
  const openProductDetail = () => setIsProductDetailOpen(true)
  const closeProductDetail = () => setIsProductDetailOpen(false)
  
  const [productToShow, setProductToShow] = useState({});


  return (
    <ShoppingCartContext.Provider
      value={{
        contador,
        setContador,
        isProductDetailOpen,
        openProductDetail,
        closeProductDetail,
        productToShow,
        setProductToShow
      }}
    > 
      {children}
    </ShoppingCartContext.Provider>
  );
}
