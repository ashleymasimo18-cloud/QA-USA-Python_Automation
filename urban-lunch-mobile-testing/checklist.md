# Urban Lunch — Test Checklist and Results

| # | Description | Status | Bug ID |
|---|---|---|---|
| 1 | Selecting a pick-up location | | |
| | The map shows the order of the pickup points | FAILED | S6P-1 |
| | Verify no pick-up point is selected by default | PASSED | |
| | Verify tapping a pick-up point highlights it and considers it selected | PASSED | |
| | A repeated tap on a pick-up point cancels the selection | PASSED | |
| | Verify selecting another pick-up point changes the selection | PASSED | |
| | Verify drop-down list is displayed | PASSED | |
| | Verify the drop-down list contains restaurant options | PASSED | |
| | Verify a restaurant can be selected from the drop-down list | PASSED | |
| | Verify selecting a restaurant from the drop-down selects the corresponding point on the map | PASSED | |
| 2 | Choice of dishes | | |
| | Verify dishes are displayed as a list | PASSED | |
| | Verify each dish displays name | PASSED | |
| | Verify each dish item displays a "+" button | PASSED | |
| | Verify each dish item displays a "-" button | PASSED | |
| | Verify each dish item displays an arrow icon | PASSED | |
| | Verify tapping a dish item (excluding the "+" button) opens the dish details screen | PASSED | |
| | Verify clicking the "+" button adds the dish to the order list | PASSED | |
| | The "Next" button is displayed in the footer | PASSED | |
| | The "Next" button is inactive if there are no dishes in the order list | PASSED | |
| | **Dish Details** | | |
| | Verify a return arrow is displayed to the left of the name of the dish | PASSED | |
| | Verify pressing return arrow navigates back to dish list | PASSED | |
| | Verify restaurant name is displayed below dish ingredients | FAILED | S6P-2 |
| | Verify tapping on the restaurant name adds the dish to order list | PASSED | |
| 3 | Order Confirmation | | |
| | Verify dish list scrolls when long | PASSED | |
| | Verify the total amount is displayed on the screen | PASSED | |
| | Verify the total amount includes the price of all selected dishes | PASSED | |
| | Verify the total amount includes the delivery cost | FAILED | S6P-3 |
| | Verify the total amount updates when a dish is added | PASSED | |
| | Verify the total amount updates when a dish is removed | PASSED | |
| | "Order" button is displayed in the footer | PASSED | |
| | Verify tapping the "Order" button takes the user to the order tracking screen | PASSED | |
| 4 | Order Tracking Screen: Order Pick-up | | |
| | Verify map displays routes from restaurants to pick-up point | PASSED | |
| | Verify the map displays the total cost of dishes per restaurant | PASSED | |
| | Verify map displays restaurants preparing dishes | PASSED | |
| | Verify the map displays remaining cooking time for each restaurant | FAILED | S6P-4 |
| | Verify the map displays remaining delivery time from each restaurant to the pick-up point | PASSED | |
| | Verify many items on the list do not fit on the order tracking screen | PASSED | |
| | Verify dish list is scrollable when long on order tracking screen | PASSED | |
| 5 | The Order is Delivered | | |
| | Verify "Order is delivered" appears automatically when timer expires | PASSED | |
| | Verify the map shows the point on the map where the desired pick-up point is located | FAILED | S6P-5 |
| | Verify a feedback bar is displayed after completing the order | PASSED | |
| | Verify user is redirected to the initial screen after order completion | PASSED | |
| | Verify user can select a new pick-up point after returning to the initial screen | PASSED | |
| | **Error Notifications** | | |
| | Verify an error message appears when geolocation access is denied | PASSED | |
| | Verify an error message appears when attempting to order without adding any dishes | PASSED | |

**Total: 44 test cases — 39 passed, 5 failed**
