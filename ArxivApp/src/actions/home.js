/* eslint-disable import/prefer-default-export */
/* eslint-disable no-unused-vars */
import API from "../service/api"
import { GET_NEW_PAPER } from "../constants/home"

export const getNewPapers = () => {
    return async dispatch => {
        let result = await API.get("posts/");
        dispatch({
          type: GET_NEW_PAPER,
          papers: result
        });
      };
  };