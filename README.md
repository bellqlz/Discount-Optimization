# Discount-Optimization
predict reactivation of customer and make schedule to maximize reactivation.


--------------------------explanation for code------------------------------------------------------------

There are many data need to analyze and deal with.

delete irrelevant data like transaction, likes.
['voucher_code_received'] and ['promotionid_received'] are duplicate, so that ['discount'] is enough to use.

delete data which has many missing values, like brithday, gender.

make normalization of data like active, discount, repurchase(only in predictionnew as prediction need to know seperately).

Finally, the relevant features are: is_seller, active and discount.
