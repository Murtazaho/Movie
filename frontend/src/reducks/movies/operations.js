import API from '../../API';
import { fetchMoviesAction } from './actions';
const api = new API();

export const fetchMovies = params => {
     console.log('the params from operation is :', params);
    return async dispatch => {
        return api
            .getMovies(params)
            .then(movies => {
                console.log(movies);
                dispatch(fetchMoviesAction(movies));
            })
            .catch(error => {
                alert('Failed to connect API: /movies/');
            });
    };
};