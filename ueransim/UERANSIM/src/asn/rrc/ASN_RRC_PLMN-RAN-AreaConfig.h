/*
 * Generated by asn1c-0.9.29 (http://lionet.info/asn1c)
 * From ASN.1 module "NR-RRC-Definitions"
 * 	found in "asn/nr-rrc-15.6.0.asn1"
 * 	`asn1c -fcompound-names -pdu=all -findirect-choice -fno-include-deps -gen-PER -no-gen-OER -no-gen-example -D rrc`
 */

#ifndef	_ASN_RRC_PLMN_RAN_AreaConfig_H_
#define	_ASN_RRC_PLMN_RAN_AreaConfig_H_


#include <asn_application.h>

/* Including external dependencies */
#include <asn_SEQUENCE_OF.h>
#include <constr_SEQUENCE_OF.h>
#include <constr_SEQUENCE.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Forward declarations */
struct ASN_RRC_PLMN_Identity;
struct ASN_RRC_RAN_AreaConfig;

/* ASN_RRC_PLMN-RAN-AreaConfig */
typedef struct ASN_RRC_PLMN_RAN_AreaConfig {
	struct ASN_RRC_PLMN_Identity	*plmn_Identity;	/* OPTIONAL */
	struct ASN_RRC_PLMN_RAN_AreaConfig__ran_Area {
		A_SEQUENCE_OF(struct ASN_RRC_RAN_AreaConfig) list;
		
		/* Context for parsing across buffer boundaries */
		asn_struct_ctx_t _asn_ctx;
	} ran_Area;
	
	/* Context for parsing across buffer boundaries */
	asn_struct_ctx_t _asn_ctx;
} ASN_RRC_PLMN_RAN_AreaConfig_t;

/* Implementation */
extern asn_TYPE_descriptor_t asn_DEF_ASN_RRC_PLMN_RAN_AreaConfig;
extern asn_SEQUENCE_specifics_t asn_SPC_ASN_RRC_PLMN_RAN_AreaConfig_specs_1;
extern asn_TYPE_member_t asn_MBR_ASN_RRC_PLMN_RAN_AreaConfig_1[2];

#ifdef __cplusplus
}
#endif

#endif	/* _ASN_RRC_PLMN_RAN_AreaConfig_H_ */
#include <asn_internal.h>
