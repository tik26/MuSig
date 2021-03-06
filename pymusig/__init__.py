"""
MuSig Implemenation for Python

This is an implementation of the muSig Proposal for schnorr multisignatures.
Paper: https://eprint.iacr.org/2018/068

Reference C implementation:
https://github.com/ElementsProject/secp256k1-zkp/tree/secp256k1-zkp/src/modules/musig
"""
from .musig import CombinedPubkey, MuSigSession

from .schnorr import schnorr_sign, schnorr_verify, schnorr_batch_verify

from .version import __version__
