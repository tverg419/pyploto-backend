import React, { useState } from 'react';
import axiosInstance from '../axios.js'

function Signup(props) {

    const initialState = {
        email: '',
        first_name: '',
        last_name: '',
        username: '',
        password: '',
    }

    const [form, setForm] = useState(initialState)

    const handleChange = (event) => {
        setForm({...form, [event.target.name]: event.target.value})
    }
    
    const handleSubmit = (event) => {
        event.preventDefault()
        axiosInstance.post('/users/create/',
        {
            email: form.email,
            first_name: form.first_name,
            last_name: form.last_name,
            username: form.username,
            password: form.password,
        })
        .then(() => {
            axiosInstance.post('token/obtain/', {
                username: form.username,
                password: form.password
            })
            .then(res => {
                axiosInstance.defaults.headers['Authorization'] = `JWT ${res.data.access}`
                localStorage.setItem('access_token', res.data.access)
                localStorage.setItem('refresh_token', res.data.refresh)
                localStorage.setItem('username', form.username)
                return res
            })
        })

        .catch(error => console.error)
        setForm(initialState)
    }

    return (
        <div>
            <h1>Sign-Up</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor='email'>Email: </label>
                <input type='email' name='email' value={form.email} onChange={handleChange}></input>
                <label htmlFor='first_name'>First Name: </label>
                <input type='text' name='first_name' value={form.first_name} onChange={handleChange}></input>
                <label htmlFor='last_name'>Last Name: </label>
                <input type='text' name='last_name' value={form.last_name} onChange={handleChange}></input>
                <label htmlFor='username'>Username: </label>
                <input type='text' name='username' value={form.username} onChange={handleChange}></input>
                <label htmlFor='password'>Password: </label>
                <input type='password' name='password'value={form.password}onChange={handleChange}></input>
                <button type='submit'>Submit</button>                
            </form>
        </div>
    );
}

export default Signup;