/*
 * Generated by asn1c-0.9.29 (http://lionet.info/asn1c)
 * From ASN.1 module "NR-InterNodeDefinitions"
 * 	found in "asn/nr-rrc-15.6.0.asn1"
 * 	`asn1c -fcompound-names -pdu=all -findirect-choice -fno-include-deps -gen-PER -no-gen-OER -no-gen-example -D rrc`
 */

#ifndef	_ASN_RRC_ConfigRestrictInfoSCG_H_
#define	_ASN_RRC_ConfigRestrictInfoSCG_H_


#include <asn_application.h>

/* Including external dependencies */
#include <NativeInteger.h>
#include "ASN_RRC_P-Max.h"
#include <constr_SEQUENCE.h>
#include "ASN_RRC_ServCellIndex.h"
#include "ASN_RRC_BandEntryIndex.h"
#include <asn_SEQUENCE_OF.h>
#include <constr_SEQUENCE_OF.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Forward declarations */
struct ASN_RRC_BandCombinationInfoList;

/* ASN_RRC_ConfigRestrictInfoSCG */
typedef struct ASN_RRC_ConfigRestrictInfoSCG {
	struct ASN_RRC_BandCombinationInfoList	*allowedBC_ListMRDC;	/* OPTIONAL */
	struct ASN_RRC_ConfigRestrictInfoSCG__powerCoordination_FR1 {
		ASN_RRC_P_Max_t	*p_maxNR_FR1;	/* OPTIONAL */
		ASN_RRC_P_Max_t	*p_maxEUTRA;	/* OPTIONAL */
		ASN_RRC_P_Max_t	*p_maxUE_FR1;	/* OPTIONAL */
		
		/* Context for parsing across buffer boundaries */
		asn_struct_ctx_t _asn_ctx;
	} *powerCoordination_FR1;
	struct ASN_RRC_ConfigRestrictInfoSCG__servCellIndexRangeSCG {
		ASN_RRC_ServCellIndex_t	 lowBound;
		ASN_RRC_ServCellIndex_t	 upBound;
		
		/* Context for parsing across buffer boundaries */
		asn_struct_ctx_t _asn_ctx;
	} *servCellIndexRangeSCG;
	long	*maxMeasFreqsSCG;	/* OPTIONAL */
	long	*maxMeasIdentitiesSCG_NR;	/* OPTIONAL */
	/*
	 * This type is extensible,
	 * possible extensions are below.
	 */
	struct ASN_RRC_ConfigRestrictInfoSCG__ext1 {
		struct ASN_RRC_ConfigRestrictInfoSCG__ext1__selectedBandEntriesMN {
			A_SEQUENCE_OF(ASN_RRC_BandEntryIndex_t) list;
			
			/* Context for parsing across buffer boundaries */
			asn_struct_ctx_t _asn_ctx;
		} *selectedBandEntriesMN;
		long	*pdcch_BlindDetectionSCG;	/* OPTIONAL */
		long	*maxNumberROHC_ContextSessionsSN;	/* OPTIONAL */
		
		/* Context for parsing across buffer boundaries */
		asn_struct_ctx_t _asn_ctx;
	} *ext1;
	
	/* Context for parsing across buffer boundaries */
	asn_struct_ctx_t _asn_ctx;
} ASN_RRC_ConfigRestrictInfoSCG_t;

/* Implementation */
extern asn_TYPE_descriptor_t asn_DEF_ASN_RRC_ConfigRestrictInfoSCG;
extern asn_SEQUENCE_specifics_t asn_SPC_ASN_RRC_ConfigRestrictInfoSCG_specs_1;
extern asn_TYPE_member_t asn_MBR_ASN_RRC_ConfigRestrictInfoSCG_1[6];

#ifdef __cplusplus
}
#endif

#endif	/* _ASN_RRC_ConfigRestrictInfoSCG_H_ */
#include <asn_internal.h>
