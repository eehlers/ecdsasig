#include "ecdsasig.h"

#include "os.h"
#include "ux.h"
#include "utils.h"

void ecdsasig(uint8_t *dataBuffer, volatile unsigned int *tx) {
    unsigned char bip32PathLength = 0x01;
    unsigned int bip32PathInt[1];
    bip32PathInt[0] = 0;
    unsigned char privateComponent[32];
    os_perso_derive_node_bip32(CX_CURVE_256K1, bip32PathInt, bip32PathLength, privateComponent, NULL);
    cx_ecfp_private_key_t private_key;
    cx_ecdsa_init_private_key(CX_CURVE_256K1, privateComponent, 32, &private_key);
    PRINTF("Using private component\n%.*H\n", 32, privateComponent);
    PRINTF("private key=\n%.*H\n", 32, private_key.d);
    os_memset(privateComponent, 0, sizeof(privateComponent));
    cx_ecfp_public_key_t public_key;
    cx_ecfp_generate_pair(CX_CURVE_256K1, &public_key, &private_key, 1);
    PRINTF("public key=\n%.*H\n", 65, public_key.W);

    unsigned int info = 0;
    char sig[100];
    PRINTF("dataBuffer=\n%.*H\n", 32, dataBuffer);
    int siglen = cx_ecdsa_sign(&private_key, CX_LAST | CX_RND_RFC6979, CX_SHA256, dataBuffer, 32, sig, 100, &info);
    PRINTF("sig=\n%.*H\n", siglen, sig);

    int ret = cx_ecdsa_verify(&public_key, CX_LAST, CX_SHA256, dataBuffer, 32, sig, siglen);
    PRINTF("ret=%d\n", ret);

    os_memmove(G_io_apdu_buffer, sig, siglen);
    *tx = siglen;
    THROW(0x9000);
}

