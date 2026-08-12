# Urban Lunch — Mobile App Manual Testing

## Overview
Manual and functional testing project for **Urban Lunch**, a food ordering mobile app. The goal was to validate the app's core ordering flow, from selecting a pickup location through order delivery, against documented product requirements and Figma design layouts.

## Tools Used
- Android Emulator (Pixel 5)
- Jira (bug tracking)
- Figma (design reference)

## Scope
Testing covered five core flows:
1. Selecting a pickup location
2. Choosing dishes
3. Order confirmation
4. Order tracking
5. Order delivery (including error notifications)

## Results Summary
- **44 test cases executed**
- **39 passed**
- **5 bugs found and logged**, each linked to its corresponding test case

## Bugs Found
| Bug ID | Area | Description |
|---|---|---|
| S6P-1 | Pickup location | The map does not show the order of the pickup points |
| S6P-2 | Dish details | Restaurant name is not displayed below dish ingredients |
| S6P-3 | Order confirmation | Total amount does not include the delivery cost |
| S6P-4 | Order tracking | Map does not display remaining cooking time for each restaurant |
| S6P-5 | Order delivery | Map does not show the point where the pickup point is located |

## Full Checklist
See [checklist.md](./checklist.md) for the complete test case list with pass/fail status.
