class PropConforme():
    @classmethod
    def verify_conf_house(ctx, land_dispute, complies_with_regulations, eligible_for_loan):
        print("Land dispute : ", land_dispute)
        print("Complies with regulations : ", complies_with_regulations)
        print("Elligible for loan : ", eligible_for_loan)
        try:
            if (land_dispute == 0) and (complies_with_regulations == 1) and (eligible_for_loan == 1):
                conform = True
            else :
                conform = False
            return conform
        except Exception as e:
            return conform
