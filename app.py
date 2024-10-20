from flask import Flask, render_template, request, jsonify
from main import MemoryAllocator

app = Flask(__name__)
allocator = MemoryAllocator(100)  # Initialize with total memory size of 100 units

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/allocate', methods=['POST'])
def allocate():
    size = int(request.form['size'])
    success = allocator.allocate(size)
    return jsonify(success=success, blocks=allocator.get_memory_blocks())

@app.route('/free', methods=['POST'])
def free():
    size = int(request.form['size'])
    success = allocator.free(size)
    return jsonify(success=success, blocks=allocator.get_memory_blocks())

if __name__ == '__main__':
    app.run(debug=True)

