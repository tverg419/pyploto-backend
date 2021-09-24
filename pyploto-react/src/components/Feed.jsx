import React, { useEffect, useState } from 'react';

function Feed(props) {

    const [posts, setPosts] = useState([])

    useEffect(() => {

        const url = 'http://localhost:8000/posts/'
        
        fetch(url)
        .then(res => res.json())
        .then(data => {
            setPosts(data)
        })
    }, [])
    console.log(posts)
    if (posts) {

        const feed = posts.map(post => {
            console.log(post)
            return (
                <div key={post.id}>
                    <p>{post.id}</p>
                    <p>{post.title}</p>
                    <p>{post.media}</p>
                    <p>{post.likes}</p>
                    <p>{post.caption}</p>
                </div>

            )
        })
        return (
            <div>
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