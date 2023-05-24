fetch("http://test.api.weniv.co.kr/mall")
    .then((data) => data.json())
    .then((data) => {
        let product_N = data.length; // Product 개수
        let all_Stock_Count = 0;
        let all_Product_Price = 0;
        for (let d of data) {
            all_Stock_Count += d.stockCount;
            all_Product_Price += d.price;
        }
        let product_Price_Average = all_Product_Price / product_N;
        console.log("전체 Product 종류의 개수 : " + product_N);
        console.log("전체 Product stockCount의 총합 : " + all_Stock_Count);
        console.log("전체 가격의 평균 : " + product_Price_Average);
    });
