import axios from "axios";
const URL = 'http://127.0.0.1:5000/api'

export const fetchAPI = async ()=>{
    try{
      const response = await axios.get(URL)
      return response.data
    }catch(err){
      return err
    }
  }