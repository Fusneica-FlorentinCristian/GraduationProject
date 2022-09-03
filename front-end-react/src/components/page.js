import {Grid} from "@mui/material";


const Page = (props) => {
    return (
        <Grid container item height="100%" flexDirection="column" p={2}>
            <Grid item>
                <h2>{props.title}</h2>
            </Grid>
            <Grid item>
                {props.children}
            </Grid>
        </Grid>
    );
}

export default Page;