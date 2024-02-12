class PropConforme():
    def verify_conf_house(ctx, land_dispute, complies_with_regulations, eligible_for_loan):
        conform = False 
        try:
            if (land_dispute == False) and (complies_with_regulations == True) and (eligible_for_loan == True):
                conform = True
            else :
                conform = False
            return conform
        except Exception as e:
            return conform
