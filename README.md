# Discount-Optimization
predict reactivation of customer and make schedule to maximize reactivation.


--------------------------explanation for prediction------------------------------------------------------------

There are many data need to analyze and deal with.

delete irrelevant data like transaction, likes.
['voucher_code_received'] and ['promotionid_received'] are duplicate, so that ['discount'] is enough to use.

delete data which has many missing values, like brithday, gender.

make normalization of data like active, discount, repurchase(only in predictionnew as prediction need to know seperately).

Finally, the relevant features are: is_seller, active and discount.

-----------------------------scheme for customer---------------------------------------------------------

In this case, I divided customers into two groups based on theie behavior before voucher is received.
Group A: low active
Group B: High active
Voucher has 3 types discount :20 with capacity of 1000000, 30 with capacity of 100000, 50 with capacity of 3000000.

From the result of optimization.code, all groups receive 50 discount voucher due to its enough capacity.


