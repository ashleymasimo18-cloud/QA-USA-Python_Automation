# Urban Grocers API — Test Checklist and Results

## Suite 1: Kits & Products (`POST /api/v1/kits/:id/products`)

| # | Test Case | Status | Bug ID |
|---|---|---|---|
| 1 | Add an existing product to a kit | PASSED | |
| 2 | Add the same existing product to a kit again | PASSED | |
| 3 | Add multiple existing products to a kit with available space | PASSED | |
| 4 | Add 29 products to a kit | PASSED | |
| 5 | Add 30 products to a kit | PASSED | |
| 6 | Cannot add 31 products to a kit | PASSED | |
| 7 | Cannot send an empty product list array | FAILED | SPRN-1 |
| 8 | Use an existing kit ID in the URL path | PASSED | |
| 9 | Cannot use a non-existent kit ID in the URL path | PASSED | |
| 10 | Cannot use long numbers in the kit ID in the URL path | FAILED | SPRN-2 |
| 11 | Cannot use letters in the kit ID in the URL path | FAILED | SPRN-3 |
| 12 | Cannot send an empty product ID value | PASSED | |
| 13 | Cannot send a non-existent product ID | FAILED | SPRN-4 |
| 14 | Cannot send a long number as the product ID | FAILED | SPRN-5 |
| 15 | Cannot send a Latin letter as the product ID | FAILED | SPRN-6 |
| 16 | Cannot send a non-Latin letter as the product ID | FAILED | SPRN-7 |
| 17 | Cannot send a special character as the product ID | PASSED | |
| 18 | Cannot send a decimal number as the product ID | FAILED | SPRN-8 |
| 19 | Cannot send a request with a missing "id" parameter | PASSED | |
| 20 | Cannot send a request with a missing "quantity" parameter | PASSED | |
| 21 | Cannot send a decimal number as the quantity | FAILED | SPRN-9 |
| 22 | Cannot send a special character as the quantity | PASSED | |
| 23 | Cannot send a non-Latin letter as the quantity | FAILED | SPRN-10 |
| 24 | Cannot send a Latin letter as the quantity | FAILED | SPRN-11 |
| 25 | Cannot send a long number as the quantity | FAILED | SPRN-12 |
| 26 | Cannot send an empty quantity value | PASSED | |

**Suite 1 total: 26 test cases — 14 passed, 12 failed**

## Suite 2: Fast Delivery (`POST /fast-delivery/v3.1.1/calculate-delivery.xml`)

| # | Test Case | Status | Bug ID |
|---|---|---|---|
| 1 | Fast delivery available when delivery time = 7 | PASSED | |
| 2 | Fast delivery available when delivery time = 21 | PASSED | |
| 3 | Fast delivery available when delivery time = 8 | PASSED | |
| 4 | Fast delivery available when delivery time = 20 | PASSED | |
| 5 | Fast delivery not available when delivery time = 1 | FAILED | SPRN-13 |
| 6 | Fast delivery not available when delivery time = 0 | FAILED | |
| 7 | Fast delivery not available when delivery time = 6 | FAILED | |
| 8 | Fast delivery not available when delivery time = 22 | FAILED | SPRN-14 |
| 9 | Fast delivery not available when delivery time = 23 | FAILED | |
| 10 | Fast delivery not available when delivery time = 24 | FAILED | |
| 11 | Delivery time cannot be Latin letters | FAILED | SPRN-15 |
| 12 | Delivery time cannot be non-Latin letters | FAILED | SPRN-16 |
| 13 | Delivery time cannot be special characters | FAILED | SPRN-17 |
| 14 | Delivery time cannot be decimals | FAILED | SPRN-18 |
| 15 | Delivery time cannot be a long number | FAILED | SPRN-19 |
| 16 | Delivery time cannot be a negative number | FAILED | SPRN-20 |
| 17 | Fast delivery available when product count = 1 | PASSED | |
| 18 | Fast delivery available when product count = 7 | PASSED | |
| 19 | Fast delivery not available when product count = 0 | FAILED | SPRN-21 |
| 20 | Fast delivery available when product count = 8 | PASSED | |
| 21 | Fast delivery available when product count = 14 | PASSED | |
| 22 | Fast delivery not available when product count = 15 | FAILED | SPRN-22 |
| 23 | Product count cannot be Latin letters | FAILED | SPRN-23 |
| 24 | Product count cannot be non-Latin letters | FAILED | SPRN-24 |
| 25 | Product count cannot be special characters | FAILED | SPRN-25 |
| 26 | Product count cannot be a negative number | FAILED | SPRN-26 |
| 27 | Product count cannot be a decimal | FAILED | SPRN-27 |
| 28 | Fast delivery available when product weight = 0 | PASSED | |
| 29 | Fast delivery available when product weight = 2.5 | PASSED | |
| 30 | Fast delivery available when product weight = 2.6 | PASSED | |
| 31 | Fast delivery available when product weight = 6 | PASSED | |
| 32 | Fast delivery available when product weight = 0.1 | PASSED | |
| 33 | Fast delivery available when product weight = 2.7 | PASSED | |
| 34 | Fast delivery available when product weight = 5.9 | PASSED | |
| 35 | Fast delivery available when product weight = 6.1 | FAILED | SPRN-28 |

**Suite 2 total: 35 test cases — 15 passed, 20 failed**

## Combined Total
**61 test cases — 29 passed, 32 failed**
