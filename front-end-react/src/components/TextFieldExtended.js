import {TextField} from "@mui/material";
import React from "react";

const TextFieldExtended = (props) => {
    return (
        <TextField size="small"
                   required
                   error={props.hasError}
                   id={props.name}
                   label={props.name}
                   defaultValue={props.defaultValue}
                   helperText={props.helperText}
                   type={props.fieldType}
                   variant="outlined"
                   onChange={props.handleChange}/>
    );
}

export default TextFieldExtended;