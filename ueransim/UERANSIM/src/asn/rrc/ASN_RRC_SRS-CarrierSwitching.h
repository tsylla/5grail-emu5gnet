/*
 * Generated by asn1c-0.9.29 (http://lionet.info/asn1c)
 * From ASN.1 module "NR-RRC-Definitions"
 * 	found in "asn/nr-rrc-15.6.0.asn1"
 * 	`asn1c -fcompound-names -pdu=all -findirect-choice -fno-include-deps -gen-PER -no-gen-OER -no-gen-example -D rrc`
 */

#ifndef	_ASN_RRC_SRS_CarrierSwitching_H_
#define	_ASN_RRC_SRS_CarrierSwitching_H_


#include <asn_application.h>

/* Including external dependencies */
#include <NativeInteger.h>
#include <NativeEnumerated.h>
#include <asn_SEQUENCE_OF.h>
#include <constr_SEQUENCE_OF.h>
#include <constr_CHOICE.h>
#include "ASN_RRC_ServCellIndex.h"
#include <constr_SEQUENCE.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Dependencies */
typedef enum ASN_RRC_SRS_CarrierSwitching__srs_SwitchFromCarrier {
	ASN_RRC_SRS_CarrierSwitching__srs_SwitchFromCarrier_sUL	= 0,
	ASN_RRC_SRS_CarrierSwitching__srs_SwitchFromCarrier_nUL	= 1
} e_ASN_RRC_SRS_CarrierSwitching__srs_SwitchFromCarrier;
typedef enum ASN_RRC_SRS_CarrierSwitching__srs_TPC_PDCCH_Group_PR {
	ASN_RRC_SRS_CarrierSwitching__srs_TPC_PDCCH_Group_PR_NOTHING,	/* No components present */
	ASN_RRC_SRS_CarrierSwitching__srs_TPC_PDCCH_Group_PR_typeA,
	ASN_RRC_SRS_CarrierSwitching__srs_TPC_PDCCH_Group_PR_typeB
} ASN_RRC_SRS_CarrierSwitching__srs_TPC_PDCCH_Group_PR;

/* Forward declarations */
struct ASN_RRC_SRS_TPC_PDCCH_Config;

/* ASN_RRC_SRS-CarrierSwitching */
typedef struct ASN_RRC_SRS_CarrierSwitching {
	long	*srs_SwitchFromServCellIndex;	/* OPTIONAL */
	long	 srs_SwitchFromCarrier;
	struct ASN_RRC_SRS_CarrierSwitching__srs_TPC_PDCCH_Group {
		ASN_RRC_SRS_CarrierSwitching__srs_TPC_PDCCH_Group_PR present;
		union ASN_RRC_SRS_CarrierSwitching__ASN_RRC_srs_TPC_PDCCH_Group_u {
			struct ASN_RRC_SRS_CarrierSwitching__srs_TPC_PDCCH_Group__typeA {
				A_SEQUENCE_OF(struct ASN_RRC_SRS_TPC_PDCCH_Config) list;
				
				/* Context for parsing across buffer boundaries */
				asn_struct_ctx_t _asn_ctx;
			} *typeA;
			struct ASN_RRC_SRS_TPC_PDCCH_Config	*typeB;
		} choice;
		
		/* Context for parsing across buffer boundaries */
		asn_struct_ctx_t _asn_ctx;
	} *srs_TPC_PDCCH_Group;
	struct ASN_RRC_SRS_CarrierSwitching__monitoringCells {
		A_SEQUENCE_OF(ASN_RRC_ServCellIndex_t) list;
		
		/* Context for parsing across buffer boundaries */
		asn_struct_ctx_t _asn_ctx;
	} *monitoringCells;
	/*
	 * This type is extensible,
	 * possible extensions are below.
	 */
	
	/* Context for parsing across buffer boundaries */
	asn_struct_ctx_t _asn_ctx;
} ASN_RRC_SRS_CarrierSwitching_t;

/* Implementation */
/* extern asn_TYPE_descriptor_t asn_DEF_ASN_RRC_srs_SwitchFromCarrier_3;	// (Use -fall-defs-global to expose) */
extern asn_TYPE_descriptor_t asn_DEF_ASN_RRC_SRS_CarrierSwitching;
extern asn_SEQUENCE_specifics_t asn_SPC_ASN_RRC_SRS_CarrierSwitching_specs_1;
extern asn_TYPE_member_t asn_MBR_ASN_RRC_SRS_CarrierSwitching_1[4];

#ifdef __cplusplus
}
#endif

#endif	/* _ASN_RRC_SRS_CarrierSwitching_H_ */
#include <asn_internal.h>
