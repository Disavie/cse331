def sort_inventory(inventory, priority):
    """
    Sorts an inventory list in-place based on a given priority order.

    This function rearranges the items in `inventory` such that all items of type `priority[0]`
    appear first, followed by all items of type `priority[1]`, and finally all items of type `priority[2]`.
    The sorting should be done in O(N) time and O(1) space.

    Parameters:
    ----------
    inventory : List[int]
        A list of item IDs representing inventory. Each item in `inventory` is guaranteed
        to be one of the three types specified in `priority`.

    priority : List[int]
        A list of exactly three distinct integers that specify the desired order
        of sorting. The items in `inventory` should be rearranged to match this order.

    Returns:
    -------
    List[int]
        The modified `inventory` list, sorted in-place according to the `priority` order.

    Example:
    -------
    >>> inventory = [2, 0, 0, 3, 3, 0, 2, 2]
    >>> priority = [0, 2, 3]
    >>> sort_inventory(inventory, priority)
    [0, 0, 0, 2, 2, 2, 3, 3]
    """


    low = mid = 0
    high = len(inventory) - 1

    while mid <= high:
        if inventory[mid] == priority[0]:
            inventory[low], inventory[mid] = inventory[mid], inventory[low]
            low += 1
            mid += 1
        elif inventory[mid] == priority[1]:
            mid += 1
        else:  # inventory[mid] == priority[2]
            inventory[mid], inventory[high] = inventory[high], inventory[mid]
            high -= 1

    return inventory

