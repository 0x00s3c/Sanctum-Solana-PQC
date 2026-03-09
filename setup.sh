#!/bin/bash

# --- 1. System Dependencies ---
echo "🚀 Installing System Dependencies..."
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    brew install cmake ninja openssl liboqs
else
    # Linux
    sudo apt-get update
    sudo apt-get install -y build-essential cmake ninja-build libssl-dev git
fi

# --- 2. Python Virtual Environment ---
echo "🐍 Setting up Python Virtual Environment..."
python3 -m venv venv
source venv/bin/activate

# --- 3. PQC Library Setup ---
echo "🔐 Building liboqs-python bindings..."
git clone --depth=1 https://github.com/open-quantum-safe/liboqs-python.git
cd liboqs-python
pip install .
cd ..

# --- 4. Install Project Requirements ---
echo "📦 Installing Python packages..."
pip install --upgrade pip
pip install -r requirements.txt

# --- 5. Verify Installation ---
echo "🔍 Verifying Stack..."
python3 -c "import oqs; print('✅ PQC (liboqs) Loaded')"
python3 -c "import pennylane; print('✅ Quantum (PennyLane) Loaded')"

echo "✨ Environment Ready! Use 'source venv/bin/activate' to begin."