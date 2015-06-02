function round(x,   ival, aval, fraction)
     {
        ival = int(x)    # integer part, int() truncates
     
        # see if fractional part
        if (ival == x)   # no fraction
           return ival   # ensure no decimals
     
        if (x < 0) {
           aval = -x     # absolute value
           ival = int(aval)
           fraction = aval - ival
           if (fraction >= .5)
              return int(x) - 1   # -2.5 --> -3
           else
              return int(x)       # -2.3 --> -2
        } else {
           fraction = x - ival
           if (fraction >= .5)
              return ival + 1
           else
              return ival
        }
     }

{ print $1 / round($1 / 22), round($1/22), $1, $2  } 
END { print "avg-size(GB)", "num-aus", "total-size(GB)", "dir" }