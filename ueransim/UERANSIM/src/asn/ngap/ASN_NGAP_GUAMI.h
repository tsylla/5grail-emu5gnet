/*
 * Generated by asn1c-0.9.29 (http://lionet.info/asn1c)
 * From ASN.1 module "NGAP-IEs"
 * 	found in "asn/ngap-15.8.0.asn1"
 * 	`asn1c -fcompound-names -pdu=all -findirect-choice -fno-include-deps -gen-PER -no-gen-OER -no-gen-example -D ngap`
 */

#ifndef	_ASN_NGAP_GUAMI_H_
#define	_ASN_NGAP_GUAMI_H_


#include <asn_application.h>

/* Including external dependencies */
#include "ASN_NGAP_PLMNIdentity.h"
#include "ASN_NGAP_AMFRegionID.h"
#include "ASN_NGAP_AMFSetID.h"
#include "ASN_NGAP_AMFPointer.h"
#include <constr_SEQUENCE.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Forward declarations */
struct ASN_NGAP_ProtocolExtensionContainer;

/* ASN_NGAP_GUAMI */
typedef struct ASN_NGAP_GUAMI {
	ASN_NGAP_PLMNIdentity_t	 pLMNIdentity;
	ASN_NGAP_AMFRegionID_t	 aMFRegionID;
	ASN_NGAP_AMFSetID_t	 aMFSetID;
	ASN_NGAP_AMFPointer_t	 aMFPointer;
	struct ASN_NGAP_ProtocolExtensionContainer	*iE_Extensions;	/* OPTIONAL */
	/*
	 * This type is extensible,
	 * possible extensions are below.
	 */
	
	/* Context for parsing across buffer boundaries */
	asn_struct_ctx_t _asn_ctx;
} ASN_NGAP_GUAMI_t;

/* Implementation */
extern asn_TYPE_descriptor_t asn_DEF_ASN_NGAP_GUAMI;
extern asn_SEQUENCE_specifics_t asn_SPC_ASN_NGAP_GUAMI_specs_1;
extern asn_TYPE_member_t asn_MBR_ASN_NGAP_GUAMI_1[5];

#ifdef __cplusplus
}
#endif

#endif	/* _ASN_NGAP_GUAMI_H_ */
#include <asn_internal.h>
