import React, {useEffect, useState} from 'react';
import "./newspage.scss"
import Circle from "../../utils/circle/Circle"
import NewsCard from "../../utils/news-card/NewsCard";
import AliceCarousel from 'react-alice-carousel';
import 'react-alice-carousel/lib/alice-carousel.css';
import axios from "axios";
import Slider from "react-slick"

interface Item {
    title: string;
    description: string;
    new_url: string;
    photo: string;
}


export const NewsPage = () => {

    const [news, setNews] = useState<Item[]>([]);

    useEffect(() => {
        axios.get('http://localhost:8000/api/v0/news/?page=1')
            .then(res => {
                setNews(res.data.news);
            }).catch(err => {
                console.log('error')
        })
    }, []);

    const responsive = {
        0: { items: 1 },
        1100: { items: 2 },
        1650: { items: 3 },
        2350: { items: 4 }
    };

    const Carousel = ({ items }: { items: Item[] }) => (
        <AliceCarousel
            mouseTracking
            items={items.map((item, index) => (
                <div key={index}> {/* Обернуть каждый элемент в <div> */}
                    <NewsCard
                        title={item.title}
                        description={item.description}
                        new_url={item.new_url}
                        photo={item.photo}
                    />
                </div>
            ))}
            controlsStrategy="alternate"
            disableButtonsControls={true}
            responsive={responsive}
            infinite={true}
        />
    );

    return (
        <section className={"news-page"}>
            <Circle title="новости"/>
            <div className="news-carousel">
                <div className="desktop-carousel">
                    <Carousel items={news}/>
                </div>
                <div className="mobile-carousel">
                    {news.map((item, index) => (
                        <NewsCard
                            key={index}
                            title={item.title}
                            description={item.description}
                            new_url={item.new_url}
                            photo={item.photo}
                        />
                    ))}
                </div>
            </div>
        </section>
    )
}
