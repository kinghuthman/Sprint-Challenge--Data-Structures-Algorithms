class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    depth = []
    depth.append(self)
    while len(depth):
        current_node = depth.pop()
        if current_node.right:
            depth.append(current_node.right)
        if current_node.left:
            depth.append(current_node.left)
        cb(current_node.value)
    

  def breadth_first_for_each(self, cb):
    breadth = []
    breadth.append(self)
    while len(breadth):
        current_node = breadth.pop(0)
        if current_node.left:
            breadth.append(current_node.left)
        if current_node.right:
            breadth.append(current_node.right)
        cb(current_node.value)

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
