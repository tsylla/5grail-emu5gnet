/*
 * Generated by asn1c-0.9.29 (http://lionet.info/asn1c)
 * From ASN.1 module "NGAP-CommonDataTypes"
 * 	found in "asn/ngap-15.8.0.asn1"
 * 	`asn1c -fcompound-names -pdu=all -findirect-choice -fno-include-deps -gen-PER -no-gen-OER -no-gen-example -D ngap`
 */

#ifndef	_ASN_NGAP_Presence_H_
#define	_ASN_NGAP_Presence_H_


#include <asn_application.h>

/* Including external dependencies */
#include <NativeEnumerated.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Dependencies */
typedef enum ASN_NGAP_Presence {
	ASN_NGAP_Presence_optional	= 0,
	ASN_NGAP_Presence_conditional	= 1,
	ASN_NGAP_Presence_mandatory	= 2
} e_ASN_NGAP_Presence;

/* ASN_NGAP_Presence */
typedef long	 ASN_NGAP_Presence_t;

/* Implementation */
extern asn_per_constraints_t asn_PER_type_ASN_NGAP_Presence_constr_1;
extern asn_TYPE_descriptor_t asn_DEF_ASN_NGAP_Presence;
extern const asn_INTEGER_specifics_t asn_SPC_ASN_NGAP_Presence_specs_1;
asn_struct_free_f ASN_NGAP_Presence_free;
asn_struct_print_f ASN_NGAP_Presence_print;
asn_constr_check_f ASN_NGAP_Presence_constraint;
ber_type_decoder_f ASN_NGAP_Presence_decode_ber;
der_type_encoder_f ASN_NGAP_Presence_encode_der;
xer_type_decoder_f ASN_NGAP_Presence_decode_xer;
xer_type_encoder_f ASN_NGAP_Presence_encode_xer;
per_type_decoder_f ASN_NGAP_Presence_decode_uper;
per_type_encoder_f ASN_NGAP_Presence_encode_uper;
per_type_decoder_f ASN_NGAP_Presence_decode_aper;
per_type_encoder_f ASN_NGAP_Presence_encode_aper;

#ifdef __cplusplus
}
#endif

#endif	/* _ASN_NGAP_Presence_H_ */
#include <asn_internal.h>
