const getLocalValue = (itemName) => {
    const storageItem = localStorage.getItem(itemName);
    return storageItem ? JSON.parse(storageItem) : {}
};

const setLocalValue = (itemName, key, value) => {
    const obj = { [key]: value };
    const storageItem = getLocalValue(itemName);
    const storageItemValue = storageItem ? { ...storageItem, ...obj} : obj;
    localStorage.setItem(itemName, JSON.stringify(storageItemValue));
};

const incLocalValue = (itemName, key, value=1) => {
    const storageItem = getLocalValue(itemName);
    const storageItemValue = storageItem[key] ? storageItem[key] : 0;
    setLocalValue(itemName, key, storageItemValue + value);
    updateCartData();

};

const decLocalValue = (itemName, key, value=1) => {
    const storageItem = getLocalValue(itemName);
    const storageItemValue = storageItem[key] ? storageItem[key] : 0;
    setLocalValue(itemName, key, storageItemValue - value)
    updateCartData();
};

const updateCartData = () => {
    const storageItem = getLocalValue('product');
    let goods_sum = 0;
    for (let k in storageItem){
        goods_sum += storageItem[k];
    }
    const cartItem = document.getElementById("cart_data");
    cartItem.innerText = goods_sum;
};