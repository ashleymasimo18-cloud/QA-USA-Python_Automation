# Urban Grocers API — API Testing & Validation

## Overview
API testing project for **Urban Grocers**, covering two endpoints: adding products to a kit, and calculating fast delivery availability and cost. Testing focused on validating expected responses, status codes, and edge cases using structured test design (boundary value analysis and equivalence partitioning).

## Tools Used
- Postman (API requests and validation)
- Jira (bug tracking)

## Scope
1. **Kits & Products endpoint** (`POST /api/v1/kits/:id/products`) — adding products to a kit, including boundary limits, invalid IDs, and invalid request body values.
2. **Fast Delivery endpoint** (`POST /fast-delivery/v3.1.1/calculate-delivery.xml`) — delivery time windows, product count, and product weight boundaries affecting delivery cost and availability.

## Results Summary
| Suite | Test Cases | Passed | Failed |
|---|---|---|---|
| Kits & Products | 26 | 14 | 12 |
| Fast Delivery | 35 | 15 | 20 |
| **Total** | **61** | **29** | **32** |

## Notable Bugs Found
| Bug ID | Area | Description |
|---|---|---|
| SPRN-1 | Kits & Products | Empty product list array is accepted (returns 200 OK instead of 400) |
| SPRN-2 | Kits & Products | Long numbers in the kit ID path param return 500 instead of 404 |
| SPRN-3 | Kits & Products | Letters in the kit ID path param return 500 instead of 404 |
| SPRN-4 | Kits & Products | Non-existent product ID is accepted (returns 200 OK instead of 400) |
| SPRN-5 to SPRN-12 | Kits & Products | Invalid product ID/quantity values (long numbers, letters, decimals) return 500 instead of 400 |
| SPRN-13, SPRN-14 | Fast Delivery | Fast delivery incorrectly reported as available at delivery-time boundaries that should be rejected |
| SPRN-15 to SPRN-20 | Fast Delivery | Invalid delivery time values (letters, symbols, decimals, long/negative numbers) are silently accepted instead of returning 400 |
| SPRN-21, SPRN-23 to SPRN-27 | Fast Delivery | Invalid or boundary product count values are silently accepted instead of returning 400 |
| SPRN-22, SPRN-28 | Fast Delivery | Delivery cost calculation returns incorrect values at product count/weight boundaries |

## Full Checklists
See [checklist.md](./checklist.md) for the complete test case list with pass/fail status for both suites.
