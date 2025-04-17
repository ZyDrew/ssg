

def markdown_to_blocks(markdown):
    #From end to top :
    # - Split on the double \n\n to separate the markdown to block of lines
    # - Split each block to individual line (separated by \n) and apply a strip() to remove starting and trailing whitespace
    # - Apply a filter function to remove from the list of lines every empty or "\n" line
    # - Apply a join on "\n" to merge lines together as a list of blocks 
    # - Apply a filter to remove excessive newline ("\n\n") within the list of blocks

    result = list(
        filter(None,                                        #None -> Delete auto all falsy elements (empty strings, None, etc.)
            map(lambda block: "\n".join(
                filter(None, 
                    map(str.strip,                          #str.strip built-in function
                        block.split("\n"))                   
                )
            ), 
            markdown.split("\n\n")
        )))
    return result