import "./App.css";
import { Grid } from "@mui/material";
import Sidebar from "./components/Sidebar";
import MainApp from "./components/MainApp";

function App() {
  return (
    <>
      <Grid container>
        <Grid item xs={4}>
          <Sidebar />
        </Grid>
        <Grid item xs={8}>
          <MainApp />
        </Grid>
      </Grid>
    </>
  );
}

export default App;
