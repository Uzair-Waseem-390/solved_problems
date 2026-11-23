# Product of the Last K Numbers
# Difficulty: Medium
# https://leetcode.com/problems/product-of-the-last-k-numbers/

# Using a prefix product array allows O(1) getProduct.
# Handling zeros is crucial: when a zero is added, it effectively resets the product chain,
# so we restart the prefix product array from [1]. If getProduct(k) requires numbers
# from before the last zero reset, the product is 0.
class ProductOfNumbers:

    def __init__(self):
        self.prefix_products = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_products = [1]
        else:
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k