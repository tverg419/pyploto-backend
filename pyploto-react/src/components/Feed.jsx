import React, { useEffect, useState } from 'react';
import axiosInstance from '../axios.js'

function Feed(props) {

    const [posts, setPosts] = useState([])

    function getPosts() {
        
        axiosInstance.get('/posts/')
        .then(res => res.json())
        .then(data => {
            console.log(data)
            setPosts(data)
        })
        .catch(err => console.error)
    }
    useEffect(() => getPosts(), [])

    if (posts) {

        const feed = posts.map(post => {
            return (
                <div key={post.id}>
                    <p>{post.title}</p>
                    <p>{post.media}</p>
                    <p>{post.likes}</p>
                    <p>{post.caption}</p>
                </div>

            )
        })
        return (
            <div>
                <h1>Post</h1>
                {feed}
            </div>
        )

    } else {

        return (
            <div>
                <p>Loading...</p>
            </div>
        )

    }

}

export default Feed;