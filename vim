### Registers ###
"ayw  /  "byy   --- yanks word into register a  /  yanks line into register b
"ap   /  "bp    --- pastes from register a  /  pastes from register b
in :%s/// --- use ^r for "

### Regex ###
# replace grep output with just line numbers
%s/^.*py:\(\d\+\).*/\1/g

# replace register "a with register "b
%s/^ra/^rb/gc

