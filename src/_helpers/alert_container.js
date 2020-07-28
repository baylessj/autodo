/**
 * Extends the default React Router history to enable redirecting users from
 * outside React components, e.g. from the user actions after a login
 */
import React, { useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { alertClear } from '../_slices';

export function RouteListener() {
  const location = useLocation();
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(alertClear());
  }, [location, dispatch]);

  return <div />;
}
