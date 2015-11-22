from sitetree.utils import tree, item

# Be sure you defined `sitetrees` in your module.
sitetrees = (
  # Define a tree with `tree` function.
  tree('produtos', items=[
      # Then define items and their children with `item` function.
      item('Categoria', 'categoria')
  ]),
  # ... You can define more than one tree for your app.
)
