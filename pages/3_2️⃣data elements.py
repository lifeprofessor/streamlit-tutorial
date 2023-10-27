import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime
from datetime import date
from datetime import time

st.write('### :blue[DataFrame]')
check1 = st.checkbox('Show DataFrame Examples', value=False)
if check1:
    df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
    st.dataframe(df)  # Same as st.write(df)
    st.code(f'''
    df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
    st.dataframe(df)  # Same as st.write(df)
            ''')
    
    df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))
    st.dataframe(df.style.highlight_max(axis=0))
    st.code(f'''
    df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))
    st.dataframe(df.style.highlight_max(axis=0))
            ''')
    
    df = pd.DataFrame(
    {
        "name": ["Roadmap", "Extras", "Issues"],
        "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
        "stars": [random.randint(0, 1000) for _ in range(3)],
        "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
    }
    )
    st.dataframe(
        df,
        column_config={
            "name": "App name",
            "stars": st.column_config.NumberColumn(
                "Github Stars",
                help="Number of stars on GitHub",
                format="%d ⭐",
            ),
            "url": st.column_config.LinkColumn("App URL"),
            "views_history": st.column_config.LineChartColumn(
                "Views (past 30 days)", y_min=0, y_max=5000
            ),
        },
        hide_index=True,
    )
    st.code('''
    df = pd.DataFrame(
        {
            "name": ["Roadmap", "Extras", "Issues"],
            "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
            "stars": [random.randint(0, 1000) for _ in range(3)],
            "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
        }
    )
    st.dataframe(
        df,
        column_config={
            "name": "App name",
            "stars": st.column_config.NumberColumn(
                "Github Stars",
                help="Number of stars on GitHub",
                format="%d ⭐",
            ),
            "url": st.column_config.LinkColumn("App URL"),
            "views_history": st.column_config.LineChartColumn(
                "Views (past 30 days)", y_min=0, y_max=5000
            ),
        },
        hide_index=True,
    )
            ''')
    

    # Cache the dataframe so it's only loaded once
    @st.cache_data
    def load_data():
        return pd.DataFrame(
            {
                "first column": [1, 2, 3, 4],
                "second column": [10, 20, 30, 40],
            }
        )

    # Boolean to resize the dataframe, stored as a session state variable
    st.checkbox("Use container width", value=False, key="use_container_width")

    df = load_data()

    # Display the dataframe and allow the user to stretch the dataframe
    # across the full width of the container, based on the checkbox value
    st.dataframe(df, use_container_width=st.session_state.use_container_width)
    st.code('''
    # Cache the dataframe so it's only loaded once
    @st.cache_data
    def load_data():
        return pd.DataFrame(
            {
                "first column": [1, 2, 3, 4],
                "second column": [10, 20, 30, 40],
            }
        )

    # Boolean to resize the dataframe, stored as a session state variable
    st.checkbox("Use container width", value=False, key="use_container_width")

    df = load_data()

    # Display the dataframe and allow the user to stretch the dataframe
    # across the full width of the container, based on the checkbox value
    st.dataframe(df, use_container_width=st.session_state.use_container_width)
            ''')

st.markdown('---')

st.write('### :blue[Data Editor]')
check2 = st.checkbox('Show Data Editor Examples', value=False)
if check2:
    df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
    )
    edited_df = st.data_editor(df)

    favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
    st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

    st.code('''
    df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
    )
    edited_df = st.data_editor(df)

    favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
    st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
            ''')
    
    df2 = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
    )
    edited_df2 = st.data_editor(df2, num_rows="dynamic")

    favorite_command = edited_df2.loc[edited_df2["rating"].idxmax()]["command"]
    st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

    st.code('''
    df2 = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
    )
    edited_df2 = st.data_editor(df2, num_rows="dynamic")

    favorite_command = edited_df2.loc[edited_df2["rating"].idxmax()]["command"]
    st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
        ''')
    
    df3 = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
    )
    edited_df3 = st.data_editor(
    df3,
    column_config={
        "command": "Streamlit Command",
        "rating": st.column_config.NumberColumn(
            "Your rating",
            help="How much do you like this command (1-5)?",
            min_value=1,
            max_value=5,
            step=1,
            format="%d ⭐",
        ),
        "is_widget": "Widget ?",
    },
    disabled=["command", "is_widget"],
    hide_index=True,
    )

    favorite_command = edited_df3.loc[edited_df["rating"].idxmax()]["command"]
    st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

    st.code('''
    df3 = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
    )
    edited_df3 = st.data_editor(
    df3,
    column_config={
        "command": "Streamlit Command",
        "rating": st.column_config.NumberColumn(
            "Your rating",
            help="How much do you like this command (1-5)?",
            min_value=1,
            max_value=5,
            step=1,
            format="%d ⭐",
        ),
        "is_widget": "Widget ?",
    },
    disabled=["command", "is_widget"],
    hide_index=True,
    )

    favorite_command = edited_df3.loc[edited_df["rating"].idxmax()]["command"]
    st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
            ''')
    
st.write('### :blue[Column Configuration]')
check3 = st.checkbox('Show Column Configuration Examples', value=True)
if check3:
    '* Column'
    data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
    }
    )

    st.data_editor(
        data_df,
        column_config={
            "widgets": st.column_config.Column(
                "Streamlit Widgets",
                help="Streamlit **widget** commands 🎈",
                width="medium",
                required=True,
            )
        },
        hide_index=True,
        num_rows="dynamic",
    )
    st.code('''
    data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
    }
    )

    st.data_editor(
        data_df,
        column_config={
            "widgets": st.column_config.Column(
                "Streamlit Widgets",
                help="Streamlit **widget** commands 🎈",
                width="medium",
                required=True,
            )
        },
        hide_index=True,
        num_rows="dynamic",
    )
            ''')
    '* TextColumn'

    data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
    }
)

    st.data_editor(
        data_df,
        column_config={
            "widgets": st.column_config.TextColumn(
                "Widgets",
                help="Streamlit **widget** commands 🎈",
                default="st.",
                max_chars=50,
                validate="^st\.[a-z_]+$",
            )
        },
        hide_index=True,
    )
    st.code('''
    data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
    }
    )

    st.data_editor(
        data_df,
        column_config={
            "widgets": st.column_config.TextColumn(
                "Widgets",
                help="Streamlit **widget** commands 🎈",
                default="st.",
                max_chars=50,
                validate="^st\.[a-z_]+$",
            )
        },
        hide_index=True,
    )
    ''')

    '* NumberColumn'
    data_df = pd.DataFrame(
    {
        "price": [20, 950, 250, 500],
    }
    )

    st.data_editor(
        data_df,
        column_config={
            "price": st.column_config.NumberColumn(
                "Price (in USD)",
                help="The price of the product in USD",
                min_value=0,
                max_value=1000,
                step=1,
                format="$%d",
            )
        },
        hide_index=True,
    )

    st.code('''
    data_df = pd.DataFrame(
    {
        "price": [20, 950, 250, 500],
    }
    )

    st.data_editor(
        data_df,
        column_config={
            "price": st.column_config.NumberColumn(
                "Price (in USD)",
                help="The price of the product in USD",
                min_value=0,
                max_value=1000,
                step=1,
                format="$%d",
            )
        },
        hide_index=True,
    )
            ''')
    '* CheckboxColumn'
    data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
        "favorite": [True, False, False, True],
    }
    )

    st.data_editor(
    data_df,
    column_config={
        "favorite": st.column_config.CheckboxColumn(
            "Your favorite?",
            help="Select your **favorite** widgets",
            default=False,
        )
    },
    disabled=["widgets"],
    hide_index=True,
    )
    st.code('''
    data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
        "favorite": [True, False, False, True],
    }
    )

    st.data_editor(
    data_df,
    column_config={
        "favorite": st.column_config.CheckboxColumn(
            "Your favorite?",
            help="Select your **favorite** widgets",
            default=False,
        )
    },
    disabled=["widgets"],
    hide_index=True,
    )
            ''')
    
    '* SelectboxColumn'
    data_df = pd.DataFrame(
    {
        "category": [
            "📊 Data Exploration",
            "📈 Data Visualization",
            "🤖 LLM",
            "📊 Data Exploration",
        ],
    }
    )

    st.data_editor(
        data_df,
        column_config={
            "category": st.column_config.SelectboxColumn(
                "App Category",
                help="The category of the app",
                width="medium",
                options=[
                    "📊 Data Exploration",
                    "📈 Data Visualization",
                    "🤖 LLM",
                ],
                required=True,
            )
        },
        hide_index=True,
    )
    st.code('''
    data_df = pd.DataFrame(
    {
        "category": [
            "📊 Data Exploration",
            "📈 Data Visualization",
            "🤖 LLM",
            "📊 Data Exploration",
        ],
    }
    )

    st.data_editor(
        data_df,
        column_config={
            "category": st.column_config.SelectboxColumn(
                "App Category",
                help="The category of the app",
                width="medium",
                options=[
                    "📊 Data Exploration",
                    "📈 Data Visualization",
                    "🤖 LLM",
                ],
                required=True,
            )
        },
        hide_index=True,
    )
            ''')
    
    '* DatetimeColumn'    
    data_df = pd.DataFrame(
    {
        "appointment": [
            datetime(2024, 2, 5, 12, 30),
            datetime(2023, 11, 10, 18, 0),
            datetime(2024, 3, 11, 20, 10),
            datetime(2023, 9, 12, 3, 0),
        ]
    }
    )

    st.data_editor(
        data_df,
        column_config={
            "appointment": st.column_config.DatetimeColumn(
                "Appointment",
                min_value=datetime(2023, 6, 1),
                max_value=datetime(2025, 1, 1),
                format="D MMM YYYY, h:mm a",
                step=60,
            ),
        },
        hide_index=True,
    )
    st.code('''
    from datetime import datetime
           
    data_df = pd.DataFrame(
    {
        "appointment": [
            datetime(2024, 2, 5, 12, 30),
            datetime(2023, 11, 10, 18, 0),
            datetime(2024, 3, 11, 20, 10),
            datetime(2023, 9, 12, 3, 0),
        ]
    }
    )

    st.data_editor(
        data_df,
        column_config={
            "appointment": st.column_config.DatetimeColumn(
                "Appointment",
                min_value=datetime(2023, 6, 1),
                max_value=datetime(2025, 1, 1),
                format="D MMM YYYY, h:mm a",
                step=60,
            ),
        },
        hide_index=True,
    )
            ''')

    '* DateColumn'
    data_df = pd.DataFrame(
    {
        "birthday": [
            date(1980, 1, 1),
            date(1990, 5, 3),
            date(1974, 5, 19),
            date(2001, 8, 17),
        ]
    }
    )

    st.data_editor(
        data_df,
        column_config={
            "birthday": st.column_config.DateColumn(
                "Birthday",
                min_value=date(1900, 1, 1),
                max_value=date(2005, 1, 1),
                format="DD.MM.YYYY",
                step=1,
            ),
        },
        hide_index=True,
    )
    st.code('''
    from datetime import date
            
    data_df = pd.DataFrame(
    {
        "birthday": [
            date(1980, 1, 1),
            date(1990, 5, 3),
            date(1974, 5, 19),
            date(2001, 8, 17),
        ]
    }
    )

    st.data_editor(
        data_df,
        column_config={
            "birthday": st.column_config.DateColumn(
                "Birthday",
                min_value=date(1900, 1, 1),
                max_value=date(2005, 1, 1),
                format="DD.MM.YYYY",
                step=1,
            ),
        },
        hide_index=True,
    )
            ''')
    
    '* TimeColumn'
    data_df = pd.DataFrame(
    {
        "appointment": [
            time(12, 30),
            time(18, 0),
            time(9, 10),
            time(16, 25),
        ]
    }
    )

    st.data_editor(
        data_df,
        column_config={
            "appointment": st.column_config.TimeColumn(
                "Appointment",
                min_value=time(8, 0, 0),
                max_value=time(19, 0, 0),
                format="hh:mm a",
                step=60,
            ),
        },
        hide_index=True,
    )
    st.code('''
    from datetime import time
            
    data_df = pd.DataFrame(
    {
        "appointment": [
            time(12, 30),
            time(18, 0),
            time(9, 10),
            time(16, 25),
        ]
    }
    )

    st.data_editor(
        data_df,
        column_config={
            "appointment": st.column_config.TimeColumn(
                "Appointment",
                min_value=time(8, 0, 0),
                max_value=time(19, 0, 0),
                format="hh:mm a",
                step=60,
            ),
        },
        hide_index=True,
    )
            ''')
    
    '* ListColumn'
    data_df = pd.DataFrame(
    {
        "sales": [
            [0, 4, 26, 80, 100, 40],
            [80, 20, 80, 35, 40, 100],
            [10, 20, 80, 80, 70, 0],
            [10, 100, 20, 100, 30, 100],
        ],
    }
    )

    st.data_editor(
        data_df,
        column_config={
            "sales": st.column_config.ListColumn(
                "Sales (last 6 months)",
                help="The sales volume in the last 6 months",
                width="medium",
            ),
        },
        hide_index=True,
    )
    st.code('''
    data_df = pd.DataFrame(
    {
        "sales": [
            [0, 4, 26, 80, 100, 40],
            [80, 20, 80, 35, 40, 100],
            [10, 20, 80, 80, 70, 0],
            [10, 100, 20, 100, 30, 100],
        ],
    }
    )

    st.data_editor(
        data_df,
        column_config={
            "sales": st.column_config.ListColumn(
                "Sales (last 6 months)",
                help="The sales volume in the last 6 months",
                width="medium",
            ),
        },
        hide_index=True,
    )
            ''')

    '* LinkColumn'
    data_df = pd.DataFrame(
    {
        "apps": [
            "https://roadmap.streamlit.app",
            "https://extras.streamlit.app",
            "https://issues.streamlit.app",
            "https://30days.streamlit.app",
        ],
    }
    )

    st.data_editor(
        data_df,
        column_config={
            "apps": st.column_config.LinkColumn(
                "Trending apps",
                help="The top trending Streamlit apps",
                validate="^https://[a-z]+\.streamlit\.app$",
                max_chars=100,
            )
        },
        hide_index=True,
    )
    st.code('''
    data_df = pd.DataFrame(
    {
        "apps": [
            "https://roadmap.streamlit.app",
            "https://extras.streamlit.app",
            "https://issues.streamlit.app",
            "https://30days.streamlit.app",
        ],
    }
    )

    st.data_editor(
        data_df,
        column_config={
            "apps": st.column_config.LinkColumn(
                "Trending apps",
                help="The top trending Streamlit apps",
                validate="^https://[a-z]+\.streamlit\.app$",
                max_chars=100,
            )
        },
        hide_index=True,
    )
            ''')
    
    '* ImageColumn'
    data_df = pd.DataFrame(
    {
        "apps": [
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/5435b8cb-6c6c-490b-9608-799b543655d3/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/6a399b09-241e-4ae7-a31f-7640dc1d181e/Home_Page.png",
        ],
    }
    )

    st.data_editor(
        data_df,
        column_config={
            "apps": st.column_config.ImageColumn(
                "Preview Image", help="Streamlit app preview screenshots"
            )
        },
        hide_index=True,
    )
    st.code('''
    data_df = pd.DataFrame(
    {
        "apps": [
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/5435b8cb-6c6c-490b-9608-799b543655d3/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/6a399b09-241e-4ae7-a31f-7640dc1d181e/Home_Page.png",
        ],
    }
    )

    st.data_editor(
        data_df,
        column_config={
            "apps": st.column_config.ImageColumn(
                "Preview Image", help="Streamlit app preview screenshots"
            )
        },
        hide_index=True,
    )
            ''')
    
    '* LineChartColumn'
    data_df = pd.DataFrame(
    {
        "sales": [
            [0, 4, 26, 80, 100, 40],
            [80, 20, 80, 35, 40, 100],
            [10, 20, 80, 80, 70, 0],
            [10, 100, 20, 100, 30, 100],
        ],
    }
    )

    st.data_editor(
        data_df,
        column_config={
            "sales": st.column_config.LineChartColumn(
                "Sales (last 6 months)",
                width="medium",
                help="The sales volume in the last 6 months",
                y_min=0,
                y_max=100,
            ),
        },
        hide_index=True,
    )
    st.code('''
    data_df = pd.DataFrame(
    {
        "sales": [
            [0, 4, 26, 80, 100, 40],
            [80, 20, 80, 35, 40, 100],
            [10, 20, 80, 80, 70, 0],
            [10, 100, 20, 100, 30, 100],
        ],
    }
    )

    st.data_editor(
        data_df,
        column_config={
            "sales": st.column_config.LineChartColumn(
                "Sales (last 6 months)",
                width="medium",
                help="The sales volume in the last 6 months",
                y_min=0,
                y_max=100,
            ),
        },
        hide_index=True,
    )
            ''')
    
    '* BarChartColumn'
    data_df = pd.DataFrame(
    {
        "sales": [
            [0, 4, 26, 80, 100, 40],
            [80, 20, 80, 35, 40, 100],
            [10, 20, 80, 80, 70, 0],
            [10, 100, 20, 100, 30, 100],
        ],
    }
    )

    st.data_editor(
        data_df,
        column_config={
            "sales": st.column_config.BarChartColumn(
                "Sales (last 6 months)",
                help="The sales volume in the last 6 months",
                y_min=0,
                y_max=100,
            ),
        },
        hide_index=True,
    )

    st.code('''
    data_df = pd.DataFrame(
    {
        "sales": [
            [0, 4, 26, 80, 100, 40],
            [80, 20, 80, 35, 40, 100],
            [10, 20, 80, 80, 70, 0],
            [10, 100, 20, 100, 30, 100],
        ],
    }
    )

    st.data_editor(
        data_df,
        column_config={
            "sales": st.column_config.BarChartColumn(
                "Sales (last 6 months)",
                help="The sales volume in the last 6 months",
                y_min=0,
                y_max=100,
            ),
        },
        hide_index=True,
    )
            ''')
    
    '* ProgressColumn'
    data_df = pd.DataFrame(
    {
        "sales": [200, 550, 1000, 80],
    }
    )

    st.data_editor(
        data_df,
        column_config={
            "sales": st.column_config.ProgressColumn(
                "Sales volume",
                help="The sales volume in USD",
                format="$%f",
                min_value=0,
                max_value=1000,
            ),
        },
        hide_index=True,
    )
    st.code('''
    data_df = pd.DataFrame(
    {
        "sales": [200, 550, 1000, 80],
    }
    )

    st.data_editor(
        data_df,
        column_config={
            "sales": st.column_config.ProgressColumn(
                "Sales volume",
                help="The sales volume in USD",
                format="$%f",
                min_value=0,
                max_value=1000,
            ),
        },
        hide_index=True,
    )
            ''')

    '* table'
    df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))
    st.table(df)

    st.code('''
    df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))
    st.table(df)
            ''')

    '* metric'
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
    st.code('''
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
            ''')
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")
    st.code('''
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")
            ''')

    st.metric(label="Gas price", value=4, delta=-0.5,
    delta_color="inverse")
    st.code('''
    st.metric(label="Gas price", value=4, delta=-0.5,
    delta_color="inverse")
                    ''')
    st.metric(label="Active developers", value=123, delta=123,
    delta_color="off")

    st.code('''
    st.metric(label="Active developers", value=123, delta=123,
    delta_color="off")
                    ''')
    
    '* JSON'

    st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
    })
    st.code('''
            st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
    })
        ''')
