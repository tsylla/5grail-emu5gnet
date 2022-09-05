/*
 * Generated by asn1c-0.9.29 (http://lionet.info/asn1c)
 * From ASN.1 module "NR-RRC-Definitions"
 * 	found in "asn/nr-rrc-15.6.0.asn1"
 * 	`asn1c -fcompound-names -pdu=all -findirect-choice -fno-include-deps -gen-PER -no-gen-OER -no-gen-example -D rrc`
 */

#ifndef	_ASN_RRC_CodebookConfig_H_
#define	_ASN_RRC_CodebookConfig_H_


#include <asn_application.h>

/* Including external dependencies */
#include <NativeInteger.h>
#include <BIT_STRING.h>
#include <constr_SEQUENCE.h>
#include <constr_CHOICE.h>
#include <NativeEnumerated.h>
#include <BOOLEAN.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Dependencies */
typedef enum ASN_RRC_CodebookConfig__codebookType_PR {
	ASN_RRC_CodebookConfig__codebookType_PR_NOTHING,	/* No components present */
	ASN_RRC_CodebookConfig__codebookType_PR_type1,
	ASN_RRC_CodebookConfig__codebookType_PR_type2
} ASN_RRC_CodebookConfig__codebookType_PR;
typedef enum ASN_RRC_CodebookConfig__codebookType__type1__subType_PR {
	ASN_RRC_CodebookConfig__codebookType__type1__subType_PR_NOTHING,	/* No components present */
	ASN_RRC_CodebookConfig__codebookType__type1__subType_PR_typeI_SinglePanel,
	ASN_RRC_CodebookConfig__codebookType__type1__subType_PR_typeI_MultiPanel
} ASN_RRC_CodebookConfig__codebookType__type1__subType_PR;
typedef enum ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts_PR {
	ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts_PR_NOTHING,	/* No components present */
	ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts_PR_two,
	ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts_PR_moreThanTwo
} ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts_PR;
typedef enum ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts__moreThanTwo__n1_n2_PR {
	ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts__moreThanTwo__n1_n2_PR_NOTHING,	/* No components present */
	ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts__moreThanTwo__n1_n2_PR_two_one_TypeI_SinglePanel_Restriction,
	ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts__moreThanTwo__n1_n2_PR_two_two_TypeI_SinglePanel_Restriction,
	ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts__moreThanTwo__n1_n2_PR_four_one_TypeI_SinglePanel_Restriction,
	ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts__moreThanTwo__n1_n2_PR_three_two_TypeI_SinglePanel_Restriction,
	ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts__moreThanTwo__n1_n2_PR_six_one_TypeI_SinglePanel_Restriction,
	ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts__moreThanTwo__n1_n2_PR_four_two_TypeI_SinglePanel_Restriction,
	ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts__moreThanTwo__n1_n2_PR_eight_one_TypeI_SinglePanel_Restriction,
	ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts__moreThanTwo__n1_n2_PR_four_three_TypeI_SinglePanel_Restriction,
	ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts__moreThanTwo__n1_n2_PR_six_two_TypeI_SinglePanel_Restriction,
	ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts__moreThanTwo__n1_n2_PR_twelve_one_TypeI_SinglePanel_Restriction,
	ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts__moreThanTwo__n1_n2_PR_four_four_TypeI_SinglePanel_Restriction,
	ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts__moreThanTwo__n1_n2_PR_eight_two_TypeI_SinglePanel_Restriction,
	ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts__moreThanTwo__n1_n2_PR_sixteen_one_TypeI_SinglePanel_Restriction
} ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts__moreThanTwo__n1_n2_PR;
typedef enum ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_MultiPanel__ng_n1_n2_PR {
	ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_MultiPanel__ng_n1_n2_PR_NOTHING,	/* No components present */
	ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_MultiPanel__ng_n1_n2_PR_two_two_one_TypeI_MultiPanel_Restriction,
	ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_MultiPanel__ng_n1_n2_PR_two_four_one_TypeI_MultiPanel_Restriction,
	ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_MultiPanel__ng_n1_n2_PR_four_two_one_TypeI_MultiPanel_Restriction,
	ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_MultiPanel__ng_n1_n2_PR_two_two_two_TypeI_MultiPanel_Restriction,
	ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_MultiPanel__ng_n1_n2_PR_two_eight_one_TypeI_MultiPanel_Restriction,
	ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_MultiPanel__ng_n1_n2_PR_four_four_one_TypeI_MultiPanel_Restriction,
	ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_MultiPanel__ng_n1_n2_PR_two_four_two_TypeI_MultiPanel_Restriction,
	ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_MultiPanel__ng_n1_n2_PR_four_two_two_TypeI_MultiPanel_Restriction
} ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_MultiPanel__ng_n1_n2_PR;
typedef enum ASN_RRC_CodebookConfig__codebookType__type2__subType_PR {
	ASN_RRC_CodebookConfig__codebookType__type2__subType_PR_NOTHING,	/* No components present */
	ASN_RRC_CodebookConfig__codebookType__type2__subType_PR_typeII,
	ASN_RRC_CodebookConfig__codebookType__type2__subType_PR_typeII_PortSelection
} ASN_RRC_CodebookConfig__codebookType__type2__subType_PR;
typedef enum ASN_RRC_CodebookConfig__codebookType__type2__subType__typeII__n1_n2_codebookSubsetRestriction_PR {
	ASN_RRC_CodebookConfig__codebookType__type2__subType__typeII__n1_n2_codebookSubsetRestriction_PR_NOTHING,	/* No components present */
	ASN_RRC_CodebookConfig__codebookType__type2__subType__typeII__n1_n2_codebookSubsetRestriction_PR_two_one,
	ASN_RRC_CodebookConfig__codebookType__type2__subType__typeII__n1_n2_codebookSubsetRestriction_PR_two_two,
	ASN_RRC_CodebookConfig__codebookType__type2__subType__typeII__n1_n2_codebookSubsetRestriction_PR_four_one,
	ASN_RRC_CodebookConfig__codebookType__type2__subType__typeII__n1_n2_codebookSubsetRestriction_PR_three_two,
	ASN_RRC_CodebookConfig__codebookType__type2__subType__typeII__n1_n2_codebookSubsetRestriction_PR_six_one,
	ASN_RRC_CodebookConfig__codebookType__type2__subType__typeII__n1_n2_codebookSubsetRestriction_PR_four_two,
	ASN_RRC_CodebookConfig__codebookType__type2__subType__typeII__n1_n2_codebookSubsetRestriction_PR_eight_one,
	ASN_RRC_CodebookConfig__codebookType__type2__subType__typeII__n1_n2_codebookSubsetRestriction_PR_four_three,
	ASN_RRC_CodebookConfig__codebookType__type2__subType__typeII__n1_n2_codebookSubsetRestriction_PR_six_two,
	ASN_RRC_CodebookConfig__codebookType__type2__subType__typeII__n1_n2_codebookSubsetRestriction_PR_twelve_one,
	ASN_RRC_CodebookConfig__codebookType__type2__subType__typeII__n1_n2_codebookSubsetRestriction_PR_four_four,
	ASN_RRC_CodebookConfig__codebookType__type2__subType__typeII__n1_n2_codebookSubsetRestriction_PR_eight_two,
	ASN_RRC_CodebookConfig__codebookType__type2__subType__typeII__n1_n2_codebookSubsetRestriction_PR_sixteen_one
} ASN_RRC_CodebookConfig__codebookType__type2__subType__typeII__n1_n2_codebookSubsetRestriction_PR;
typedef enum ASN_RRC_CodebookConfig__codebookType__type2__subType__typeII_PortSelection__portSelectionSamplingSize {
	ASN_RRC_CodebookConfig__codebookType__type2__subType__typeII_PortSelection__portSelectionSamplingSize_n1	= 0,
	ASN_RRC_CodebookConfig__codebookType__type2__subType__typeII_PortSelection__portSelectionSamplingSize_n2	= 1,
	ASN_RRC_CodebookConfig__codebookType__type2__subType__typeII_PortSelection__portSelectionSamplingSize_n3	= 2,
	ASN_RRC_CodebookConfig__codebookType__type2__subType__typeII_PortSelection__portSelectionSamplingSize_n4	= 3
} e_ASN_RRC_CodebookConfig__codebookType__type2__subType__typeII_PortSelection__portSelectionSamplingSize;
typedef enum ASN_RRC_CodebookConfig__codebookType__type2__phaseAlphabetSize {
	ASN_RRC_CodebookConfig__codebookType__type2__phaseAlphabetSize_n4	= 0,
	ASN_RRC_CodebookConfig__codebookType__type2__phaseAlphabetSize_n8	= 1
} e_ASN_RRC_CodebookConfig__codebookType__type2__phaseAlphabetSize;
typedef enum ASN_RRC_CodebookConfig__codebookType__type2__numberOfBeams {
	ASN_RRC_CodebookConfig__codebookType__type2__numberOfBeams_two	= 0,
	ASN_RRC_CodebookConfig__codebookType__type2__numberOfBeams_three	= 1,
	ASN_RRC_CodebookConfig__codebookType__type2__numberOfBeams_four	= 2
} e_ASN_RRC_CodebookConfig__codebookType__type2__numberOfBeams;

/* ASN_RRC_CodebookConfig */
typedef struct ASN_RRC_CodebookConfig {
	struct ASN_RRC_CodebookConfig__codebookType {
		ASN_RRC_CodebookConfig__codebookType_PR present;
		union ASN_RRC_CodebookConfig__ASN_RRC_codebookType_u {
			struct ASN_RRC_CodebookConfig__codebookType__type1 {
				struct ASN_RRC_CodebookConfig__codebookType__type1__subType {
					ASN_RRC_CodebookConfig__codebookType__type1__subType_PR present;
					union ASN_RRC_CodebookConfig__ASN_RRC_codebookType__ASN_RRC_type1__ASN_RRC_subType_u {
						struct ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel {
							struct ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts {
								ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts_PR present;
								union ASN_RRC_CodebookConfig__ASN_RRC_codebookType__ASN_RRC_type1__ASN_RRC_subType__ASN_RRC_typeI_SinglePanel__ASN_RRC_nrOfAntennaPorts_u {
									struct ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts__two {
										BIT_STRING_t	 twoTX_CodebookSubsetRestriction;
										
										/* Context for parsing across buffer boundaries */
										asn_struct_ctx_t _asn_ctx;
									} *two;
									struct ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts__moreThanTwo {
										struct ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts__moreThanTwo__n1_n2 {
											ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts__moreThanTwo__n1_n2_PR present;
											union ASN_RRC_CodebookConfig__ASN_RRC_codebookType__ASN_RRC_type1__ASN_RRC_subType__ASN_RRC_typeI_SinglePanel__ASN_RRC_nrOfAntennaPorts__ASN_RRC_moreThanTwo__ASN_RRC_n1_n2_u {
												BIT_STRING_t	 two_one_TypeI_SinglePanel_Restriction;
												BIT_STRING_t	 two_two_TypeI_SinglePanel_Restriction;
												BIT_STRING_t	 four_one_TypeI_SinglePanel_Restriction;
												BIT_STRING_t	 three_two_TypeI_SinglePanel_Restriction;
												BIT_STRING_t	 six_one_TypeI_SinglePanel_Restriction;
												BIT_STRING_t	 four_two_TypeI_SinglePanel_Restriction;
												BIT_STRING_t	 eight_one_TypeI_SinglePanel_Restriction;
												BIT_STRING_t	 four_three_TypeI_SinglePanel_Restriction;
												BIT_STRING_t	 six_two_TypeI_SinglePanel_Restriction;
												BIT_STRING_t	 twelve_one_TypeI_SinglePanel_Restriction;
												BIT_STRING_t	 four_four_TypeI_SinglePanel_Restriction;
												BIT_STRING_t	 eight_two_TypeI_SinglePanel_Restriction;
												BIT_STRING_t	 sixteen_one_TypeI_SinglePanel_Restriction;
											} choice;
											
											/* Context for parsing across buffer boundaries */
											asn_struct_ctx_t _asn_ctx;
										} n1_n2;
										BIT_STRING_t	*typeI_SinglePanel_codebookSubsetRestriction_i2;	/* OPTIONAL */
										
										/* Context for parsing across buffer boundaries */
										asn_struct_ctx_t _asn_ctx;
									} *moreThanTwo;
								} choice;
								
								/* Context for parsing across buffer boundaries */
								asn_struct_ctx_t _asn_ctx;
							} nrOfAntennaPorts;
							BIT_STRING_t	 typeI_SinglePanel_ri_Restriction;
							
							/* Context for parsing across buffer boundaries */
							asn_struct_ctx_t _asn_ctx;
						} *typeI_SinglePanel;
						struct ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_MultiPanel {
							struct ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_MultiPanel__ng_n1_n2 {
								ASN_RRC_CodebookConfig__codebookType__type1__subType__typeI_MultiPanel__ng_n1_n2_PR present;
								union ASN_RRC_CodebookConfig__ASN_RRC_codebookType__ASN_RRC_type1__ASN_RRC_subType__ASN_RRC_typeI_MultiPanel__ASN_RRC_ng_n1_n2_u {
									BIT_STRING_t	 two_two_one_TypeI_MultiPanel_Restriction;
									BIT_STRING_t	 two_four_one_TypeI_MultiPanel_Restriction;
									BIT_STRING_t	 four_two_one_TypeI_MultiPanel_Restriction;
									BIT_STRING_t	 two_two_two_TypeI_MultiPanel_Restriction;
									BIT_STRING_t	 two_eight_one_TypeI_MultiPanel_Restriction;
									BIT_STRING_t	 four_four_one_TypeI_MultiPanel_Restriction;
									BIT_STRING_t	 two_four_two_TypeI_MultiPanel_Restriction;
									BIT_STRING_t	 four_two_two_TypeI_MultiPanel_Restriction;
								} choice;
								
								/* Context for parsing across buffer boundaries */
								asn_struct_ctx_t _asn_ctx;
							} ng_n1_n2;
							BIT_STRING_t	 ri_Restriction;
							
							/* Context for parsing across buffer boundaries */
							asn_struct_ctx_t _asn_ctx;
						} *typeI_MultiPanel;
					} choice;
					
					/* Context for parsing across buffer boundaries */
					asn_struct_ctx_t _asn_ctx;
				} subType;
				long	 codebookMode;
				
				/* Context for parsing across buffer boundaries */
				asn_struct_ctx_t _asn_ctx;
			} *type1;
			struct ASN_RRC_CodebookConfig__codebookType__type2 {
				struct ASN_RRC_CodebookConfig__codebookType__type2__subType {
					ASN_RRC_CodebookConfig__codebookType__type2__subType_PR present;
					union ASN_RRC_CodebookConfig__ASN_RRC_codebookType__ASN_RRC_type2__ASN_RRC_subType_u {
						struct ASN_RRC_CodebookConfig__codebookType__type2__subType__typeII {
							struct ASN_RRC_CodebookConfig__codebookType__type2__subType__typeII__n1_n2_codebookSubsetRestriction {
								ASN_RRC_CodebookConfig__codebookType__type2__subType__typeII__n1_n2_codebookSubsetRestriction_PR present;
								union ASN_RRC_CodebookConfig__ASN_RRC_codebookType__ASN_RRC_type2__ASN_RRC_subType__ASN_RRC_typeII__ASN_RRC_n1_n2_codebookSubsetRestriction_u {
									BIT_STRING_t	 two_one;
									BIT_STRING_t	 two_two;
									BIT_STRING_t	 four_one;
									BIT_STRING_t	 three_two;
									BIT_STRING_t	 six_one;
									BIT_STRING_t	 four_two;
									BIT_STRING_t	 eight_one;
									BIT_STRING_t	 four_three;
									BIT_STRING_t	 six_two;
									BIT_STRING_t	 twelve_one;
									BIT_STRING_t	 four_four;
									BIT_STRING_t	 eight_two;
									BIT_STRING_t	 sixteen_one;
								} choice;
								
								/* Context for parsing across buffer boundaries */
								asn_struct_ctx_t _asn_ctx;
							} n1_n2_codebookSubsetRestriction;
							BIT_STRING_t	 typeII_RI_Restriction;
							
							/* Context for parsing across buffer boundaries */
							asn_struct_ctx_t _asn_ctx;
						} *typeII;
						struct ASN_RRC_CodebookConfig__codebookType__type2__subType__typeII_PortSelection {
							long	*portSelectionSamplingSize;	/* OPTIONAL */
							BIT_STRING_t	 typeII_PortSelectionRI_Restriction;
							
							/* Context for parsing across buffer boundaries */
							asn_struct_ctx_t _asn_ctx;
						} *typeII_PortSelection;
					} choice;
					
					/* Context for parsing across buffer boundaries */
					asn_struct_ctx_t _asn_ctx;
				} subType;
				long	 phaseAlphabetSize;
				BOOLEAN_t	 subbandAmplitude;
				long	 numberOfBeams;
				
				/* Context for parsing across buffer boundaries */
				asn_struct_ctx_t _asn_ctx;
			} *type2;
		} choice;
		
		/* Context for parsing across buffer boundaries */
		asn_struct_ctx_t _asn_ctx;
	} codebookType;
	
	/* Context for parsing across buffer boundaries */
	asn_struct_ctx_t _asn_ctx;
} ASN_RRC_CodebookConfig_t;

/* Implementation */
/* extern asn_TYPE_descriptor_t asn_DEF_ASN_RRC_portSelectionSamplingSize_57;	// (Use -fall-defs-global to expose) */
/* extern asn_TYPE_descriptor_t asn_DEF_ASN_RRC_phaseAlphabetSize_63;	// (Use -fall-defs-global to expose) */
/* extern asn_TYPE_descriptor_t asn_DEF_ASN_RRC_numberOfBeams_67;	// (Use -fall-defs-global to expose) */
extern asn_TYPE_descriptor_t asn_DEF_ASN_RRC_CodebookConfig;
extern asn_SEQUENCE_specifics_t asn_SPC_ASN_RRC_CodebookConfig_specs_1;
extern asn_TYPE_member_t asn_MBR_ASN_RRC_CodebookConfig_1[1];

#ifdef __cplusplus
}
#endif

#endif	/* _ASN_RRC_CodebookConfig_H_ */
#include <asn_internal.h>