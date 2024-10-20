class Block:
    def __init__(self, size):
        self.size = size
        self.is_free = True
        self.next = None

class MemoryAllocator:
    def __init__(self, total_size):
        self.head = Block(total_size)

    def allocate(self, size):
        current = self.head
        while current:
            if current.is_free and current.size >= size:
                if current.size > size:
                    new_block = Block(current.size - size)
                    new_block.next = current.next
                    current.next = new_block
                current.size = size
                current.is_free = False
                return True
            current = current.next
        return False

    def free(self, size):
        current = self.head
        while current:
            if not current.is_free and current.size == size:
                current.is_free = True
                self.merge_free_blocks()
                return True
            current = current.next
        return False

    def merge_free_blocks(self):
        current = self.head
        while current and current.next:
            if current.is_free and current.next.is_free:
                current.size += current.next.size
                current.next = current.next.next
            else:
                current = current.next

    def get_memory_blocks(self):
        blocks = []
        current = self.head
        while current:
            blocks.append({"size": current.size, "is_free": current.is_free})
            current = current.next
        return blocks


