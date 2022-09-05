/*
 * Generated by asn1c-0.9.29 (http://lionet.info/asn1c)
 * From ASN.1 module "NR-RRC-Definitions"
 * 	found in "asn/nr-rrc-15.6.0.asn1"
 * 	`asn1c -fcompound-names -pdu=all -findirect-choice -fno-include-deps -gen-PER -no-gen-OER -no-gen-example -D rrc`
 */

#ifndef	_ASN_RRC_Phy_ParametersFR2_H_
#define	_ASN_RRC_Phy_ParametersFR2_H_


#include <asn_application.h>

/* Including external dependencies */
#include <NativeEnumerated.h>
#include <constr_SEQUENCE.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Dependencies */
typedef enum ASN_RRC_Phy_ParametersFR2__dummy {
	ASN_RRC_Phy_ParametersFR2__dummy_supported	= 0
} e_ASN_RRC_Phy_ParametersFR2__dummy;
typedef enum ASN_RRC_Phy_ParametersFR2__pdsch_RE_MappingFR2_PerSymbol {
	ASN_RRC_Phy_ParametersFR2__pdsch_RE_MappingFR2_PerSymbol_n6	= 0,
	ASN_RRC_Phy_ParametersFR2__pdsch_RE_MappingFR2_PerSymbol_n20	= 1
} e_ASN_RRC_Phy_ParametersFR2__pdsch_RE_MappingFR2_PerSymbol;
typedef enum ASN_RRC_Phy_ParametersFR2__ext1__pCell_FR2 {
	ASN_RRC_Phy_ParametersFR2__ext1__pCell_FR2_supported	= 0
} e_ASN_RRC_Phy_ParametersFR2__ext1__pCell_FR2;
typedef enum ASN_RRC_Phy_ParametersFR2__ext1__pdsch_RE_MappingFR2_PerSlot {
	ASN_RRC_Phy_ParametersFR2__ext1__pdsch_RE_MappingFR2_PerSlot_n16	= 0,
	ASN_RRC_Phy_ParametersFR2__ext1__pdsch_RE_MappingFR2_PerSlot_n32	= 1,
	ASN_RRC_Phy_ParametersFR2__ext1__pdsch_RE_MappingFR2_PerSlot_n48	= 2,
	ASN_RRC_Phy_ParametersFR2__ext1__pdsch_RE_MappingFR2_PerSlot_n64	= 3,
	ASN_RRC_Phy_ParametersFR2__ext1__pdsch_RE_MappingFR2_PerSlot_n80	= 4,
	ASN_RRC_Phy_ParametersFR2__ext1__pdsch_RE_MappingFR2_PerSlot_n96	= 5,
	ASN_RRC_Phy_ParametersFR2__ext1__pdsch_RE_MappingFR2_PerSlot_n112	= 6,
	ASN_RRC_Phy_ParametersFR2__ext1__pdsch_RE_MappingFR2_PerSlot_n128	= 7,
	ASN_RRC_Phy_ParametersFR2__ext1__pdsch_RE_MappingFR2_PerSlot_n144	= 8,
	ASN_RRC_Phy_ParametersFR2__ext1__pdsch_RE_MappingFR2_PerSlot_n160	= 9,
	ASN_RRC_Phy_ParametersFR2__ext1__pdsch_RE_MappingFR2_PerSlot_n176	= 10,
	ASN_RRC_Phy_ParametersFR2__ext1__pdsch_RE_MappingFR2_PerSlot_n192	= 11,
	ASN_RRC_Phy_ParametersFR2__ext1__pdsch_RE_MappingFR2_PerSlot_n208	= 12,
	ASN_RRC_Phy_ParametersFR2__ext1__pdsch_RE_MappingFR2_PerSlot_n224	= 13,
	ASN_RRC_Phy_ParametersFR2__ext1__pdsch_RE_MappingFR2_PerSlot_n240	= 14,
	ASN_RRC_Phy_ParametersFR2__ext1__pdsch_RE_MappingFR2_PerSlot_n256	= 15
} e_ASN_RRC_Phy_ParametersFR2__ext1__pdsch_RE_MappingFR2_PerSlot;

/* ASN_RRC_Phy-ParametersFR2 */
typedef struct ASN_RRC_Phy_ParametersFR2 {
	long	*dummy;	/* OPTIONAL */
	long	*pdsch_RE_MappingFR2_PerSymbol;	/* OPTIONAL */
	/*
	 * This type is extensible,
	 * possible extensions are below.
	 */
	struct ASN_RRC_Phy_ParametersFR2__ext1 {
		long	*pCell_FR2;	/* OPTIONAL */
		long	*pdsch_RE_MappingFR2_PerSlot;	/* OPTIONAL */
		
		/* Context for parsing across buffer boundaries */
		asn_struct_ctx_t _asn_ctx;
	} *ext1;
	
	/* Context for parsing across buffer boundaries */
	asn_struct_ctx_t _asn_ctx;
} ASN_RRC_Phy_ParametersFR2_t;

/* Implementation */
/* extern asn_TYPE_descriptor_t asn_DEF_ASN_RRC_dummy_2;	// (Use -fall-defs-global to expose) */
/* extern asn_TYPE_descriptor_t asn_DEF_ASN_RRC_pdsch_RE_MappingFR2_PerSymbol_4;	// (Use -fall-defs-global to expose) */
/* extern asn_TYPE_descriptor_t asn_DEF_ASN_RRC_pCell_FR2_9;	// (Use -fall-defs-global to expose) */
/* extern asn_TYPE_descriptor_t asn_DEF_ASN_RRC_pdsch_RE_MappingFR2_PerSlot_11;	// (Use -fall-defs-global to expose) */
extern asn_TYPE_descriptor_t asn_DEF_ASN_RRC_Phy_ParametersFR2;
extern asn_SEQUENCE_specifics_t asn_SPC_ASN_RRC_Phy_ParametersFR2_specs_1;
extern asn_TYPE_member_t asn_MBR_ASN_RRC_Phy_ParametersFR2_1[3];

#ifdef __cplusplus
}
#endif

#endif	/* _ASN_RRC_Phy_ParametersFR2_H_ */
#include <asn_internal.h>
