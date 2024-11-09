# TODO : REMOVE THIS
import json
from datetime import datetime, timedelta

# Sample input data as a JSON string
input_data = """
[
    {
        "id": 3257870,
        "name": "Sri Lanka to win the 1st T20I vs New Zealand?",
        "display_name": "Sri Lanka to win the 1st T20I vs New Zealand?",
        "is_event_active": true,
        "is_event_active_int": 1,
        "image_url": "https://probo.gumlet.io/image/upload/probo_product_images/IMAGE_0ac97fdf-55b5-49c7-9b07-108b9a6898af.png",
        "type": "probabilistic",
        "underlying_events": null,
        "yes_price": "₹ 6",
        "no_price": "₹ 4",
        "last_traded_price_for_yes": 6,
        "last_traded_price_for_no": 4,
        "user_qty_limit": 100,
        "tick_size": 0.5,
        "price_upper_limit": 9.5,
        "price_lower_limit": 0.5,
        "total_event_trade_price": 10,
        "default_qty": 1,
        "people_trading_image_url": "https://probo.gumlet.io/image/upload/probo_product_images/Bar_Chart.png",
        "yes_btn_text": "Yes",
        "no_btn_text": "No",
        "oneliner": {
            "text": "H2H last 5 T20 : SL 1 ,  New Zealand 3, DRAW 1",
            "icon": "https://probo.gumlet.io/image/upload/probo_product_images/probo_logo.png"
        },
        "ltp": null,
        "event_templated_type": "DOUBLE_ROW_PRICE",
        "event_footer": {
            "expandable_section": null
        },
        "enable_challenge": 0,
        "trading_info": "30423 traders",
        "traders_count_numeric": 30423,
        "expiry_date": "Answer will come in 8 hours",
        "expiry_date_time_stamp": "2024-11-09T20:30:00.000Z",
        "tag": [],
        "tag_list": [],
        "available_yes_price": 4,
        "available_no_price": 6,
        "slug": "sri-lanka-to-win-the-1st-t20i-vs-new-zealand-a2zrx",
        "buy_button": {
            "text": "Yes ₹6",
            "bg_color": "#F1F7FF",
            "text_color": "#197BFF",
            "opinion_text": "Yes"
        },
        "sell_button": {
            "text": "No ₹4",
            "bg_color": "#FEF6F5",
            "text_color": "#E05852",
            "opinion_text": "No"
        },
        "probability_data": {
            "text": "PROBABILITY",
            "value": 60
        },
        "bottom_stripe": null,
        "oneliner_version": "oneliner_v2",
        "oneliner_v2": {
            "text": "H2H last 5 T20 : SL 1 ,  New Zealand 3, DRAW 1",
            "icon": "https://probo.gumlet.io/image/upload/probo_product_images/probo_logo.png",
            "suffix": "Read more",
            "suffix_color": "#197BFF",
            "is_enabled": true,
            "on_click": {
                "action": "bottomsheet",
                "navigation_context": {
                    "action": "API",
                    "endpoint": "/api/v3/product/events/metadata/3257870?filters=overview,sourceOfTruth,rules",
                    "method": "GET",
                    "web_url": ""
                }
            }
        }
    },
    {
        "id": 3263317,
        "name": "Bitcoin to be priced at 76347.38 USDT or more at 06:20 PM?",
        "display_name": "Bitcoin to be priced at 76347.38 USDT or more at 06:20 PM?",
        "is_event_active": true,
        "is_event_active_int": 1,
        "image_url": "https://probo.gumlet.io/image/upload/probo_product_images/IMAGE_207fe0ff-6e8a-474a-a762-08ebbf2e36b8.png",
        "type": "probabilistic",
        "underlying_events": null,
        "yes_price": "₹ 5.5",
        "no_price": "₹ 4.5",
        "last_traded_price_for_yes": 5.5,
        "last_traded_price_for_no": 4.5,
        "user_qty_limit": 100,
        "tick_size": 0.5,
        "price_upper_limit": 9.5,
        "price_lower_limit": 0.5,
        "total_event_trade_price": 10,
        "default_qty": 1,
        "people_trading_image_url": "https://probo.gumlet.io/image/upload/probo_product_images/Bar_Chart.png",
        "yes_btn_text": "Yes",
        "no_btn_text": "No",
        "oneliner": {
            "text": "Bitcoin open price at 06:10 PM was 76347.38USDT.",
            "icon": "https://probo.gumlet.io/image/upload/probo_product_images/probo_logo.png"
        },
        "ltp": null,
        "event_templated_type": "DOUBLE_ROW_PRICE",
        "event_footer": {
            "expandable_section": null
        },
        "enable_challenge": 0,
        "trading_info": "42 traders",
        "traders_count_numeric": 42,
        "expiry_date": "Answer will come in 9 minutes",
        "expiry_date_time_stamp": "2024-11-09T12:50:00.000Z",
        "tag": [],
        "tag_list": [],
        "available_yes_price": 4.5,
        "available_no_price": 5.5,
        "slug": "bitcoin-to-be-priced-at-7634738-usdt-or-more-at-0620-pm-oaywy",
        "buy_button": {
            "text": "Yes ₹5.5",
            "bg_color": "#F1F7FF",
            "text_color": "#197BFF",
            "opinion_text": "Yes"
        },
        "sell_button": {
            "text": "No ₹4.5",
            "bg_color": "#FEF6F5",
            "text_color": "#E05852",
            "opinion_text": "No"
        },
        "probability_data": {
            "text": "PROBABILITY",
            "value": 55
        },
        "bottom_stripe": null,
        "oneliner_version": "oneliner_v2",
        "oneliner_v2": {
            "text": "Bitcoin open price at 06:10 PM was 76347.38USDT.",
            "icon": "https://probo.gumlet.io/image/upload/probo_product_images/probo_logo.png",
            "suffix": "Read more",
            "suffix_color": "#197BFF",
            "is_enabled": true,
            "on_click": {
                "action": "bottomsheet",
                "navigation_context": {
                    "action": "API",
                    "endpoint": "/api/v3/product/events/metadata/3263317?filters=overview,sourceOfTruth,rules",
                    "method": "GET",
                    "web_url": ""
                }
            }
        }
    },
    {
        "id": 3261272,
        "name": "Gautam Gambhir to remain as the head coach for Team India in Test cricket until 31st January, 2025?",
        "display_name": "Gautam Gambhir to remain as the head coach for Team India in Test cricket until 31st January, 2025?",
        "is_event_active": true,
        "is_event_active_int": 1,
        "image_url": "https://probo.gumlet.io/image/upload/probo_product_images/IMAGE_73b71c32-97bc-4030-b003-c047ccc18be9.png",
        "type": "probabilistic",
        "underlying_events": null,
        "yes_price": "₹ 6",
        "no_price": "₹ 4",
        "last_traded_price_for_yes": 6,
        "last_traded_price_for_no": 4,
        "user_qty_limit": 100,
        "tick_size": 0.5,
        "price_upper_limit": 9.5,
        "price_lower_limit": 0.5,
        "total_event_trade_price": 10,
        "default_qty": 1,
        "people_trading_image_url": "https://probo.gumlet.io/image/upload/probo_product_images/Bar_Chart.png",
        "yes_btn_text": "Yes",
        "no_btn_text": "No",
        "oneliner": {
            "text": "Gautam Gambhir was appointed as the head coach of the Indian men's cricket team on July 9, 2024.",
            "icon": "https://probo.gumlet.io/image/upload/probo_product_images/probo_logo.png"
        },
        "ltp": null,
        "event_templated_type": "DOUBLE_ROW_PRICE",
        "event_footer": {
            "expandable_section": null
        },
        "enable_challenge": 0,
        "trading_info": "62 traders",
        "traders_count_numeric": 62,
        "expiry_date": "Answer will come in 3 months",
        "expiry_date_time_stamp": "2025-01-31T18:29:00.000Z",
        "tag": [],
        "tag_list": [],
        "available_yes_price": 4,
        "available_no_price": 6,
        "slug": "gautam-gambhir-to-remain-as-the-head-coach-for-team-india-in-test-cricket-until-31st-january-2025-qqaz8",
        "buy_button": {
            "text": "Yes ₹6",
            "bg_color": "#F1F7FF",
            "text_color": "#197BFF",
            "opinion_text": "Yes"
        },
        "sell_button": {
            "text": "No ₹4",
            "bg_color": "#FEF6F5",
            "text_color": "#E05852",
            "opinion_text": "No"
        },
        "probability_data": {
            "text": "PROBABILITY",
            "value": 60
        },
        "bottom_stripe": null,
        "oneliner_version": "oneliner_v2",
        "oneliner_v2": {
            "text": "Gautam Gambhir was appointed as the head coach of the Indian men's cricket team on July 9, 2024.",
            "icon": "https://probo.gumlet.io/image/upload/probo_product_images/probo_logo.png",
            "suffix": "Read more",
            "suffix_color": "#197BFF",
            "is_enabled": true,
            "on_click": {
                "action": "bottomsheet",
                "navigation_context": {
                    "action": "API",
                    "endpoint": "/api/v3/product/events/metadata/3261272?filters=overview,sourceOfTruth,rules",
                    "method": "GET",
                    "web_url": ""
                }
            }
        }
    },
    {
        "id": 3263283,
        "name": "Ethereum to be priced at 3041.19 USDT or more at 06:20 PM?",
        "display_name": "Ethereum to be priced at 3041.19 USDT or more at 06:20 PM?",
        "is_event_active": true,
        "is_event_active_int": 1,
        "image_url": "https://probo.gumlet.io/image/upload/probo_product_images/IMAGE_5b8def5e-113c-45e9-8c87-3d28346930f7.png",
        "type": "probabilistic",
        "underlying_events": null,
        "yes_price": "₹ 3.5",
        "no_price": "₹ 6.5",
        "last_traded_price_for_yes": 3.5,
        "last_traded_price_for_no": 6.5,
        "user_qty_limit": 100,
        "tick_size": 0.5,
        "price_upper_limit": 9.5,
        "price_lower_limit": 0.5,
        "total_event_trade_price": 10,
        "default_qty": 1,
        "people_trading_image_url": "https://probo.gumlet.io/image/upload/probo_product_images/Bar_Chart.png",
        "yes_btn_text": "Yes",
        "no_btn_text": "No",
        "oneliner": {
            "text": "Ethereum open price at 06:00 PM was 3041.19USDT.",
            "icon": "https://probo.gumlet.io/image/upload/probo_product_images/probo_logo.png"
        },
        "ltp": null,
        "event_templated_type": "DOUBLE_ROW_PRICE",
        "event_footer": {
            "expandable_section": null
        },
        "enable_challenge": 0,
        "trading_info": "50 traders",
        "traders_count_numeric": 50,
        "expiry_date": "Answer will come in 9 minutes",
        "expiry_date_time_stamp": "2024-11-09T12:50:00.000Z",
        "tag": [],
        "tag_list": [],
        "available_yes_price": 6.5,
        "available_no_price": 3.5,
        "slug": "ethereum-to-be-priced-at-304119-usdt-or-more-at-0620-pm-nlbg2",
        "buy_button": {
            "text": "Yes ₹3.5",
            "bg_color": "#F1F7FF",
            "text_color": "#197BFF",
            "opinion_text": "Yes"
        },
        "sell_button": {
            "text": "No ₹6.5",
            "bg_color": "#FEF6F5",
            "text_color": "#E05852",
            "opinion_text": "No"
        },
        "probability_data": {
            "text": "PROBABILITY",
            "value": 35
        },
        "bottom_stripe": null,
        "oneliner_version": "oneliner_v2",
        "oneliner_v2": {
            "text": "Ethereum open price at 06:00 PM was 3041.19USDT.",
            "icon": "https://probo.gumlet.io/image/upload/probo_product_images/probo_logo.png",
            "suffix": "Read more",
            "suffix_color": "#197BFF",
            "is_enabled": true,
            "on_click": {
                "action": "bottomsheet",
                "navigation_context": {
                    "action": "API",
                    "endpoint": "/api/v3/product/events/metadata/3263283?filters=overview,sourceOfTruth,rules",
                    "method": "GET",
                    "web_url": ""
                }
            }
        }
    },
    {
        "id": 3263256,
        "name": "'Sourav Joshi - Ghar Aisa Hoga' video to have views between 4.111M and 4.303M at 12:00 AM?",
        "display_name": "'Sourav Joshi - Ghar Aisa Hoga' video to have views between 4.111M and 4.303M at 12:00 AM?",
        "is_event_active": true,
        "is_event_active_int": 1,
        "image_url": "https://probo.gumlet.io/image/upload/probo_product_images/IMAGE_0e5ab7d2-70d3-497d-bf0b-76455ab14364.png",
        "type": "probabilistic",
        "underlying_events": null,
        "yes_price": "₹ 8.5",
        "no_price": "₹ 1.5",
        "last_traded_price_for_yes": 8.5,
        "last_traded_price_for_no": 1.5,
        "user_qty_limit": 100,
        "tick_size": 0.5,
        "price_upper_limit": 9.5,
        "price_lower_limit": 0.5,
        "total_event_trade_price": 10,
        "default_qty": 1,
        "people_trading_image_url": "https://probo.gumlet.io/image/upload/probo_product_images/Bar_Chart.png",
        "yes_btn_text": "Yes",
        "no_btn_text": "No",
        "oneliner": {
            "text": "Current Views Rate is 13.887K | Predicted Views as per Current Rate is 3.329M | Data as of 4:50 PM - 4:55 PM",
            "icon": "https://probo.gumlet.io/image/upload/probo_product_images/probo_logo.png"
        },
        "ltp": null,
        "event_templated_type": "DOUBLE_ROW_PRICE",
        "event_footer": {
            "expandable_section": null
        },
        "enable_challenge": 0,
        "trading_info": "190 traders",
        "traders_count_numeric": 190,
        "expiry_date": "Answer will come in 6 hours",
        "expiry_date_time_stamp": "2024-11-09T18:30:00.000Z",
        "tag": [],
        "tag_list": [],
        "available_yes_price": 1.5,
        "available_no_price": 8.5,
        "slug": "sourav-joshi-ghar-aisa-hoga-video-to-have-views-between-4111m-and-4303m-at-1200-am-qkevq",
        "buy_button": {
            "text": "Yes ₹8.5",
            "bg_color": "#F1F7FF",
            "text_color": "#197BFF",
            "opinion_text": "Yes"
        },
        "sell_button": {
            "text": "No ₹1.5",
            "bg_color": "#FEF6F5",
            "text_color": "#E05852",
            "opinion_text": "No"
        },
        "probability_data": {
            "text": "PROBABILITY",
            "value": 85
        },
        "bottom_stripe": null,
        "oneliner_version": "oneliner_v2",
        "oneliner_v2": {
            "text": "Current Views Rate is 13.887K | Predicted Views as per Current Rate is 3.329M | Data as of 4:50 PM - 4:55 PM",
            "icon": "https://probo.gumlet.io/image/upload/probo_product_images/probo_logo.png",
            "suffix": "Read more",
            "suffix_color": "#197BFF",
            "is_enabled": true,
            "on_click": {
                "action": "bottomsheet",
                "navigation_context": {
                    "action": "API",
                    "endpoint": "/api/v3/product/events/metadata/3263256?filters=overview,sourceOfTruth,rules",
                    "method": "GET",
                    "web_url": ""
                }
            }
        }
    },
    {
        "id": 3263293,
        "name": "Bitcoin to be priced at 76346.54 USDT or more at 06:15 PM?",
        "display_name": "Bitcoin to be priced at 76346.54 USDT or more at 06:15 PM?",
        "is_event_active": true,
        "is_event_active_int": 1,
        "image_url": "https://probo.gumlet.io/image/upload/probo_product_images/IMAGE_207fe0ff-6e8a-474a-a762-08ebbf2e36b8.png",
        "type": "probabilistic",
        "underlying_events": null,
        "yes_price": "₹ 4.5",
        "no_price": "₹ 5.5",
        "last_traded_price_for_yes": 4.5,
        "last_traded_price_for_no": 5.5,
        "user_qty_limit": 100,
        "tick_size": 0.5,
        "price_upper_limit": 9.5,
        "price_lower_limit": 0.5,
        "total_event_trade_price": 10,
        "default_qty": 1,
        "people_trading_image_url": "https://probo.gumlet.io/image/upload/probo_product_images/Bar_Chart.png",
        "yes_btn_text": "Yes",
        "no_btn_text": "No",
        "oneliner": {
            "text": "Bitcoin open price at 06:05 PM was 76346.54USDT.",
            "icon": "https://probo.gumlet.io/image/upload/probo_product_images/probo_logo.png"
        },
        "ltp": null,
        "event_templated_type": "DOUBLE_ROW_PRICE",
        "event_footer": {
            "expandable_section": null
        },
        "enable_challenge": 0,
        "trading_info": "519 traders",
        "traders_count_numeric": 519,
        "expiry_date": "Answer will come in 4 minutes",
        "expiry_date_time_stamp": "2024-11-09T12:45:00.000Z",
        "tag": [],
        "tag_list": [],
        "available_yes_price": 5.5,
        "available_no_price": 4.5,
        "slug": "bitcoin-to-be-priced-at-7634654-usdt-or-more-at-0615-pm-p0lgx",
        "buy_button": {
            "text": "Yes ₹4.5",
            "bg_color": "#F1F7FF",
            "text_color": "#197BFF",
            "opinion_text": "Yes"
        },
        "sell_button": {
            "text": "No ₹5.5",
            "bg_color": "#FEF6F5",
            "text_color": "#E05852",
            "opinion_text": "No"
        },
        "probability_data": {
            "text": "PROBABILITY",
            "value": 45
        },
        "bottom_stripe": null,
        "oneliner_version": "oneliner_v2",
        "oneliner_v2": {
            "text": "Bitcoin open price at 06:05 PM was 76346.54USDT.",
            "icon": "https://probo.gumlet.io/image/upload/probo_product_images/probo_logo.png",
            "suffix": "Read more",
            "suffix_color": "#197BFF",
            "is_enabled": true,
            "on_click": {
                "action": "bottomsheet",
                "navigation_context": {
                    "action": "API",
                    "endpoint": "/api/v3/product/events/metadata/3263293?filters=overview,sourceOfTruth,rules",
                    "method": "GET",
                    "web_url": ""
                }
            }
        }
    },
    {
        "id": 3259298,
        "name": "Afghanistan to win the 2nd ODI vs Bangladesh?",
        "display_name": "Afghanistan to win the 2nd ODI vs Bangladesh?",
        "is_event_active": true,
        "is_event_active_int": 1,
        "image_url": "https://probo.gumlet.io/image/upload/probo_product_images/IMAGE_0260b173-1401-4a44-9b7d-3735b4c30fc2.png",
        "type": "probabilistic",
        "underlying_events": null,
        "yes_price": "₹ 5",
        "no_price": "₹ 5",
        "last_traded_price_for_yes": 5,
        "last_traded_price_for_no": 5,
        "user_qty_limit": 100,
        "tick_size": 0.5,
        "price_upper_limit": 9.5,
        "price_lower_limit": 0.5,
        "total_event_trade_price": 10,
        "default_qty": 1,
        "people_trading_image_url": "https://probo.gumlet.io/image/upload/probo_product_images/Bar_Chart.png",
        "yes_btn_text": "Yes",
        "no_btn_text": "No",
        "oneliner": {
            "text": "H2H last 5 ODI : AFG 2 ,  Bangladesh 3, DRAW 0",
            "icon": "https://probo.gumlet.io/image/upload/probo_product_images/probo_logo.png"
        },
        "ltp": null,
        "event_templated_type": "DOUBLE_ROW_PRICE",
        "event_footer": {
            "expandable_section": null
        },
        "enable_challenge": 0,
        "trading_info": "19361 traders",
        "traders_count_numeric": 19361,
        "expiry_date": "Answer will come in 8 hours",
        "expiry_date_time_stamp": "2024-11-09T21:00:00.000Z",
        "tag": [],
        "tag_list": [],
        "available_yes_price": 5,
        "available_no_price": 5,
        "slug": "afghanistan-to-win-the-2nd-odi-vs-bangladesh-px3yj",
        "buy_button": {
            "text": "Yes ₹5",
            "bg_color": "#F1F7FF",
            "text_color": "#197BFF",
            "opinion_text": "Yes"
        },
        "sell_button": {
            "text": "No ₹5",
            "bg_color": "#FEF6F5",
            "text_color": "#E05852",
            "opinion_text": "No"
        },
        "probability_data": {
            "text": "PROBABILITY",
            "value": 50
        },
        "bottom_stripe": null,
        "oneliner_version": "oneliner_v2",
        "oneliner_v2": {
            "text": "H2H last 5 ODI : AFG 2 ,  Bangladesh 3, DRAW 0",
            "icon": "https://probo.gumlet.io/image/upload/probo_product_images/probo_logo.png",
            "suffix": "Read more",
            "suffix_color": "#197BFF",
            "is_enabled": true,
            "on_click": {
                "action": "bottomsheet",
                "navigation_context": {
                    "action": "API",
                    "endpoint": "/api/v3/product/events/metadata/3259298?filters=overview,sourceOfTruth,rules",
                    "method": "GET",
                    "web_url": ""
                }
            }
        }
    },
    {
        "id": 3259362,
        "name": "Chennai to win against Mumbai?",
        "display_name": "Chennai to win against Mumbai?",
        "is_event_active": true,
        "is_event_active_int": 1,
        "image_url": "https://probo.gumlet.io/image/upload/probo_product_images/IMAGE_2b39f3ec-8e14-472b-ab36-6a1523e9e5bd.png",
        "type": "probabilistic",
        "underlying_events": null,
        "yes_price": "₹ 2",
        "no_price": "₹ 8",
        "last_traded_price_for_yes": 2,
        "last_traded_price_for_no": 8,
        "user_qty_limit": 100,
        "tick_size": 0.5,
        "price_upper_limit": 9.5,
        "price_lower_limit": 0.5,
        "total_event_trade_price": 10,
        "default_qty": 1,
        "people_trading_image_url": "https://probo.gumlet.io/image/upload/probo_product_images/Bar_Chart.png",
        "yes_btn_text": "Yes",
        "no_btn_text": "No",
        "oneliner": {
            "text": "current score: CFC-0 | MCFC-0 | Clock-53’",
            "icon": "https://probo.gumlet.io/image/upload/probo_product_images/probo_logo.png"
        },
        "ltp": null,
        "event_templated_type": "DOUBLE_ROW_PRICE",
        "event_footer": {
            "expandable_section": null
        },
        "enable_challenge": 0,
        "trading_info": "1717 traders",
        "traders_count_numeric": 1717,
        "expiry_date": "Answer will come in 2 hours",
        "expiry_date_time_stamp": "2024-11-09T15:00:00.000Z",
        "tag": [],
        "tag_list": [],
        "available_yes_price": 8,
        "available_no_price": 2,
        "slug": "chennai-to-win-against-mumbai-ly0z5",
        "buy_button": {
            "text": "Yes ₹2",
            "bg_color": "#F1F7FF",
            "text_color": "#197BFF",
            "opinion_text": "Yes"
        },
        "sell_button": {
            "text": "No ₹8",
            "bg_color": "#FEF6F5",
            "text_color": "#E05852",
            "opinion_text": "No"
        },
        "probability_data": {
            "text": "PROBABILITY",
            "value": 20
        },
        "bottom_stripe": null,
        "oneliner_version": "oneliner_v2",
        "oneliner_v2": {
            "text": "current score: CFC-0 | MCFC-0 | Clock-53’",
            "icon": "https://probo.gumlet.io/image/upload/probo_product_images/probo_logo.png",
            "suffix": "Read more",
            "suffix_color": "#197BFF",
            "is_enabled": true,
            "on_click": {
                "action": "bottomsheet",
                "navigation_context": {
                    "action": "API",
                    "endpoint": "/api/v3/product/events/metadata/3259362?filters=overview,sourceOfTruth,rules",
                    "method": "GET",
                    "web_url": ""
                }
            }
        }
    },
    {
        "id": 3250552,
        "name": "Elon Musk to be part a of Trump’s Cabinet?",
        "display_name": "Elon Musk to be part a of Trump’s Cabinet?",
        "is_event_active": true,
        "is_event_active_int": 1,
        "image_url": "https://probo.gumlet.io/image/upload/probo_product_images/IMAGE_75e29482-7c73-4b5e-b180-d3b69dfef5f7.png",
        "type": "probabilistic",
        "underlying_events": null,
        "yes_price": "₹ 3.5",
        "no_price": "₹ 6.5",
        "last_traded_price_for_yes": 3.5,
        "last_traded_price_for_no": 6.5,
        "user_qty_limit": 100,
        "tick_size": 0.5,
        "price_upper_limit": 9.5,
        "price_lower_limit": 0.5,
        "total_event_trade_price": 10,
        "default_qty": 1,
        "people_trading_image_url": "https://probo.gumlet.io/image/upload/probo_product_images/Bar_Chart.png",
        "yes_btn_text": "Yes",
        "no_btn_text": "No",
        "oneliner": {
            "text": "Musk could also play an influential role in a second Trump administration, as an adviser on spending cuts or in a more substantial way",
            "icon": "https://probo.gumlet.io/image/upload/probo_product_images/probo_logo.png"
        },
        "ltp": null,
        "event_templated_type": "DOUBLE_ROW_PRICE",
        "event_footer": {
            "expandable_section": null
        },
        "enable_challenge": 0,
        "trading_info": "3594 traders",
        "traders_count_numeric": 3594,
        "expiry_date": "Answer will come in 2 months",
        "expiry_date_time_stamp": "2025-01-20T18:29:00",
        "tag": [],
        "tag_list": [],
        "available_yes_price": 6.5,
        "available_no_price": 3.5,
        "slug": "elon-musk-to-be-part-a-of-trumps-cabinet-wqzar",
        "buy_button": {
            "text": "Yes ₹3.5",
            "bg_color": "#F1F7FF",
            "text_color": "#197BFF",
            "opinion_text": "Yes"
        },
        "sell_button": {
            "text": "No ₹6.5",
            "bg_color": "#FEF6F5",
            "text_color": "#E05852",
            "opinion_text": "No"
        },
        "probability_data": {
            "text": "PROBABILITY",
            "value": 35
        },
        "bottom_stripe": null,
        "oneliner_version": "oneliner_v2",
        "oneliner_v2": {
            "text": "Musk could also play an influential role in a second Trump administration, as an adviser on spending cuts or in a more s...",
            "icon": "https://probo.gumlet.io/image/upload/probo_product_images/probo_logo.png",
            "suffix": "Read more",
            "suffix_color": "#197BFF",
            "is_enabled": true,
            "on_click": {
                "action": "bottomsheet",
                "navigation_context": {
                    "action": "API",
                    "endpoint": "/api/v3/product/events/metadata/3250552?filters=overview,sourceOfTruth,rules",
                    "method": "GET",
                    "web_url": ""
                }
            }
        }
    },
    {
        "id": 3259613,
        "name": "Hyderabad to win the kabaddi match against Pune?",
        "display_name": "Hyderabad to win the kabaddi match against Pune?",
        "is_event_active": true,
        "is_event_active_int": 1,
        "image_url": "https://probo.gumlet.io/image/upload/probo_product_images/IMAGE_d4c81c09-75a2-4d9f-9471-1f410c3e1913.png",
        "type": "probabilistic",
        "underlying_events": null,
        "yes_price": "₹ 3.5",
        "no_price": "₹ 6.5",
        "last_traded_price_for_yes": 3.5,
        "last_traded_price_for_no": 6.5,
        "user_qty_limit": 100,
        "tick_size": 0.5,
        "price_upper_limit": 9.5,
        "price_lower_limit": 0.5,
        "total_event_trade_price": 10,
        "default_qty": 1,
        "people_trading_image_url": "https://probo.gumlet.io/image/upload/probo_product_images/Bar_Chart.png",
        "yes_btn_text": "Yes",
        "no_btn_text": "No",
        "oneliner": {
            "text": "Form (Last 5 Games): Hyderabad -  W W W L L | Pune -  W W D W L",
            "icon": "https://probo.gumlet.io/image/upload/probo_product_images/probo_logo.png"
        },
        "ltp": null,
        "event_templated_type": "DOUBLE_ROW_PRICE",
        "event_footer": {
            "expandable_section": null
        },
        "enable_challenge": 0,
        "trading_info": "3688 traders",
        "traders_count_numeric": 3688,
        "expiry_date": "Answer will come in 4 hours",
        "expiry_date_time_stamp": "2024-11-09T16:30:00.000Z",
        "tag": [],
        "tag_list": [],
        "available_yes_price": 6.5,
        "available_no_price": 3.5,
        "slug": "hyderabad-to-win-the-kabaddi-match-against-pune-mlzn5",
        "buy_button": {
            "text": "Yes ₹3.5",
            "bg_color": "#F1F7FF",
            "text_color": "#197BFF",
            "opinion_text": "Yes"
        },
        "sell_button": {
            "text": "No ₹6.5",
            "bg_color": "#FEF6F5",
            "text_color": "#E05852",
            "opinion_text": "No"
        },
        "probability_data": {
            "text": "PROBABILITY",
            "value": 35
        },
        "bottom_stripe": null,
        "oneliner_version": "oneliner_v2",
        "oneliner_v2": {
            "text": "Form (Last 5 Games): Hyderabad -  W W W L L | Pune -  W W D W L",
            "icon": "https://probo.gumlet.io/image/upload/probo_product_images/probo_logo.png",
            "suffix": "Read more",
            "suffix_color": "#197BFF",
            "is_enabled": true,
            "on_click": {
                "action": "bottomsheet",
                "navigation_context": {
                    "action": "API",
                    "endpoint": "/api/v3/product/events/metadata/3259613?filters=overview,sourceOfTruth,rules",
                    "method": "GET",
                    "web_url": ""
                }
            }
        }
    }
]
"""

# Function to infer currency from price string
def infer_currency(price_str):
    if price_str.startswith("₹"):
        return "INR"
    elif price_str.startswith("$"):
        return "USD"
    elif price_str.startswith("€"):
        return "EUR"
    # Add more currency symbols as needed
    else:
        return "USD"  # Default currency

# Function to parse team stats from oneliner text
def parse_team_stats(oneliner_text):
    team_stats = {}
    try:
        # Example oneliner_text: "H2H last 5 T20 : SL 1 ,  New Zealand 3, DRAW 1"
        parts = oneliner_text.split(":")
        if len(parts) > 1:
            scores_part = parts[1]
            scores = scores_part.split(",")
            for score in scores:
                score = score.strip()
                if " " in score:
                    team, value = score.rsplit(" ", 1)
                    team_stats[team] = {"score": int(value)}
    except Exception as e:
        print(f"Error parsing team stats: {e}")
    return team_stats

# Load the input data
try:
    events = json.loads(input_data)
except json.JSONDecodeError as e:
    print(f"Invalid JSON input: {e}")
    events = []

# Initialize the output list
output_events = []

# Iterate over each event and map to the new format
for event in events:
    new_event = {}
    
    # 1. Event Name
    new_event["event_name"] = event.get("name", "N/A")
    
    # 2. Category (Assuming 'type' corresponds to 'category')
    new_event["category"] = event.get("type", "General")
    
    # 3. End Time
    expiry_timestamp = event.get("expiry_date_time_stamp", "")
    new_event["end_time"] = expiry_timestamp
    
    # 4. Start Time (Assuming the event starts 2 hours before expiry)
    try:
        end_time_dt = datetime.strptime(expiry_timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
        start_time_dt = end_time_dt - timedelta(hours=2)
        new_event["start_time"] = start_time_dt.strftime("%Y-%m-%dT%H:%M:%S")
    except (ValueError, KeyError):
        new_event["start_time"] = "N/A"
    
    # 5. Outcome (Using a generic term or parsing from 'name')
    new_event["outcome"] = "Victory"
    
    # 6. Description (Using 'oneliner.text')
    new_event["description"] = event.get("oneliner", {}).get("text", "No description available.")
    
    # 7. Venue Stats (Placeholder as data is not available)
    new_event["venue_stats"] = "Indoor stadium, 500 seats"
    
    # 8. Team Stats (Parsed from 'oneliner.text')
    oneliner_text = event.get("oneliner", {}).get("text", "")
    new_event["team_stats"] = parse_team_stats(oneliner_text) if oneliner_text else {}
    
    # 9. Is Active
    new_event["is_active"] = event.get("is_event_active", False)
    
    # 10. Price Lower Limit
    new_event["price_lower_limit"] = event.get("price_lower_limit", 0.0)
    
    # 11. Price Upper Limit
    new_event["price_upper_limit"] = event.get("price_upper_limit", 0.0)
    
    # 12. Currency (Inferred from 'yes_price')
    yes_price = event.get("yes_price", "")
    new_event["currency"] = infer_currency(yes_price)
    
    # 13. Last Traded Price for Yes
    new_event["last_traded_price_for_yes"] = event.get("last_traded_price_for_yes", 0.0)
    
    # 14. Last Traded Price for No
    new_event["last_traded_price_for_no"] = event.get("last_traded_price_for_no", 0.0)
    
    # 15. Total Event Trade Price
    new_event["total_event_trade_price"] = event.get("total_event_trade_price", 0.0)
    
    # 16. Traders Count (Converted to string)
    new_event["traders_count"] = str(event.get("traders_count_numeric", 0))
    
    # 17. Event Slug
    slug = event.get("slug", "")
    new_event["event_slug"] = slug
    
    # 18. Share Link (Constructed using the slug)
    new_event["share_link"] = f"http://example.com/event/{slug}" if slug else "http://example.com/event/"
    new_event["image_url"] = event["image_url"]
    
    # Append the transformed event to the output list
    output_events.append(new_event)

# Output the transformed data as JSON
output_json = json.dumps(output_events, indent=4)
print(output_json)
