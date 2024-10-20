import unittest
from app import MemoryAllocator  # Adjust import if your MemoryAllocator is in another file

class TestMemoryAllocator(unittest.TestCase):

    def setUp(self):
        """Set up a new MemoryAllocator with a total size of 100 units for each test."""
        self.allocator = MemoryAllocator(100)  # Pass total size

    def test_allocate_memory(self):
        """Test allocating memory blocks."""
        self.assertTrue(self.allocator.allocate(30), "Should allocate 30 units")
        self.assertFalse(self.allocator.allocate(80), "Should not allocate 80 units, not enough space")
        self.assertTrue(self.allocator.allocate(50), "Should allocate 50 units")
        self.assertTrue(self.allocator.allocate(20), "Should allocate 20 units after splitting")

    def test_free_memory(self):
        """Test freeing memory blocks."""
        self.allocator.allocate(30)
        self.allocator.allocate(20)
        self.assertTrue(self.allocator.free(20), "Should free 20 units")
        self.assertFalse(self.allocator.free(40), "Should not free 40 units, size mismatch")
        self.assertTrue(self.allocator.free(30), "Should free 30 units")

    def test_merge_free_blocks(self):
        """Test that adjacent free blocks are merged correctly."""
        self.allocator.allocate(30)
        self.allocator.free(30)  # Free the 30 units
        self.allocator.allocate(20)  # Allocate 20 units
        self.allocator.free(20)  # Free the 20 units
        self.allocator.allocate(50)  # Allocate 50 units
        self.allocator.free(50)  # Free 50 units

        # After merging, there should be a single block of 100 units
        self.assertTrue(self.allocator.head.is_free, "The block should be free")
        self.assertEqual(self.allocator.head.size, 100, "The block size should be 100 after merging")

if __name__ == '__main__':
    unittest.main()

