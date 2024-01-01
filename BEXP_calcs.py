import math

# Valid Level Range
MIN_LEVEL           =   1
MAX_DISP_LVL_BEORC  =   20
MAX_TRUE_LVL_BEORC  =   60
MAX_DISP_LVL_LAGUZ  =   40
MAX_TRUE_LVL_LAGUZ  =   40
MIN_EXP             =   0
MAX_EXP             =   99

# Valid Tier Ranges (Laguz vs. Beorc)
MAX_TIERS_BEORC     =   3
MAX_TIERS_LAGUZ     =   1
LVLS_PER_TIER       =   20

# Difficulty Mode Multiplier
DIFF_MOD_EASY   =   2/3
DIFF_MOD_NORMAL =   1
DIFF_MOD_HARD   =   2

# Level Modifiers
LVL_MOD_BEORC   =   1
LVL_MOD_LAGUZ   =   1.5

# Return values
SUCCESS         =   0
FAILURE         =   1
INVALID_LVLS    =  -1

# Misc Constants
AUDIO_ON        =   1
AUDIO_OFF       =   0
RACE_BEORC      =   0
RACE_LAGUZ      =   1

# Calculate BEXP Requirements to go from level to level
def calc_bexp_cost(start_lvl, start_exp, end_lvl, end_exp, lvl_mod, diff_mod, race):
    # Check that level selection was valid
    if(validate_level_exp(start_lvl, start_exp, end_lvl, end_exp, race)):
        return INVALID_LVLS
    
    start_partial = False
    end_partial = False
    
    # Account for first/last level being partial
    if(start_exp > MIN_EXP):
        start_partial = True
        start_prop = ((100-start_exp)/100)  # Proportion of level remaining
    if(end_exp > MIN_EXP):
        end_partial = True
        end_prop = (end_exp/100)            # Proportion of level remaining

    # Calculate total BEXP cost by summing BEXP cost at each level
    total = 0
    # Calculate first (partial) level
    if(start_partial):
        total += (start_prop * diff_mod * ((50*(lvl_mod*(start_lvl)+1))+50))
        start_lvl += 1

    # Calculate total cost for all full levels
    for lvl in range(start_lvl, end_lvl):
        total += (diff_mod * ((50 * (lvl_mod*(lvl)+1))+50))

    # Calculate last (partial) level
    if(end_partial):
        total += (end_prop * diff_mod * ((50*(lvl_mod*(end_lvl)+1))+50))

    # Last minute rounding or sumn idk 
    # (refined through testing/comparing to real game)
    return round(total)
    
# Calculates max tier, level, and EXP reached with given amount of BEXP as input
# Returns a string for displaying all 3 fields
def calc_max_attainable_lvl(true_lvl, exp, bexp, lvl_mod, diff_mod, race):
    # Check if at max level
    if(race == RACE_BEORC):
        max_true_lvl = MAX_TRUE_LVL_BEORC
    elif(race == RACE_LAGUZ):
        max_true_lvl = MAX_TRUE_LVL_LAGUZ

    # Start calcing finals
    final_lvl = true_lvl
    final_exp = exp
    starting_bexp = bexp
    total_cost = 0

    if(true_lvl < max_true_lvl):
        # Only do calcs if under max level
        if(exp > 0):
            exp_prop = ((100-exp)/100)
        else:
            exp_prop = 1
        next_lvl_cost = exp_prop * diff_mod * ((50*(lvl_mod*(final_lvl)+1))+50)
        bexp -= next_lvl_cost
        while((bexp >= 0) and (final_lvl < max_true_lvl)):
            final_lvl += 1
            total_cost += next_lvl_cost
            next_lvl_cost = diff_mod * ((50*(lvl_mod*(final_lvl)+1))+50)
            bexp -= next_lvl_cost
        if(final_lvl < max_true_lvl):
            # Calc exp at final level
            bexp += next_lvl_cost
            final_exp = math.floor(100*(bexp/next_lvl_cost))
            total_cost += math.ceil(next_lvl_cost*(final_exp/100))
        else:
            final_exp = 0
    else:
        final_exp = 0

    bexp_leftover = starting_bexp - total_cost
    # Prepare return values for string
    if(race == RACE_BEORC):
        if(final_lvl == max_true_lvl):
            final_tier = MAX_TIERS_BEORC
            final_lvl = MAX_DISP_LVL_BEORC
        else:
            final_tier = math.ceil(final_lvl/LVLS_PER_TIER)
            final_lvl = final_lvl % LVLS_PER_TIER
        return f"Tier {final_tier}, Lvl {final_lvl}, {final_exp} Exp ({int(bexp_leftover)} BEXP Leftover)"
    elif(race == RACE_LAGUZ):
        return f"Lvl {final_lvl}, {final_exp} Exp ({int(bexp_leftover)} BEXP Leftover)"
        

# Check valid level range
# returns 0 on success, 1 on failure
def validate_level_exp(start_lvl, start_exp, end_lvl, end_exp, race):
    if(race == RACE_BEORC):
        max_true_lvl = MAX_TRUE_LVL_BEORC
    else:
        max_true_lvl = MAX_TRUE_LVL_LAGUZ
    if(start_lvl < MIN_LEVEL):
        return FAILURE
    if(end_lvl > max_true_lvl):
        return FAILURE
    if(end_lvl < start_lvl):
        return FAILURE
    if((end_lvl == max_true_lvl) and (end_exp > MIN_EXP)):
        return FAILURE
    if((start_lvl == end_lvl) and (start_exp > end_exp)):
        return FAILURE
    return SUCCESS

def convertToInternalLevel(tier, disp_lvl):
    return (tier*20) + disp_lvl