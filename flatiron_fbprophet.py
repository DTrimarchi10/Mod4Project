import pandas as pd
from fbprophet import Prophet as proph

def get_ROI_FBprophet(ts,periods,plot=False,plot_components=False,plot_title=None):
    '''
    Get forecasted ROI based on number of periods from end of ts.
    
    '''
    
    df = pd.DataFrame(ts)
    df.reset_index(inplace=True)
    df.columns = ['ds','y']
    
    model = proph(interval_width=0.95)
    model.fit(df)
    
    future_dates = model.make_future_dataframe(periods=periods,freq='MS')
    forecast = model.predict(future_dates)
    
    pred_end_val = forecast[-1:]['yhat'].values[0]
    start_val = df[-1:]['y'].values[0]
    roi = (pred_end_val - start_val) / start_val
    
    if plot:
        model.plot(forecast,uncertainty=True);
        plt.title(plot_title);
        plt.show();
        
    
    if plot_components:
        model.plot_components(forecast);
        plt.title(plot_title);
        plt.show();
    
    return roi