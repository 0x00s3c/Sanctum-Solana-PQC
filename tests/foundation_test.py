import unittest
from bridge_agent.pqc_signing import PQCSigner

class TestBridgeFoundation(unittest.TestCase):
    def test_pqc_integrity(self):
        """Validates that ML-DSA can sign/verify local vendor data."""
        signer = PQCSigner()
        payload = b"VENDOR_ID:77;AMOUNT:5.0;NONCE:9928"
        
        with oqs.Signature(signer.alg) as verifier:
            pk, sig = signer.create_pqc_auth(payload)
            is_valid = verifier.verify(payload, sig, pk)
            self.assertTrue(is_valid, "PQC Foundation Failure: Signature Invalid")
            print("✅ P2P Security Foundation: PQC signature verified locally.")

if __name__ == "__main__":
    unittest.main()