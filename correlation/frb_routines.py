import matplotlib
matplotlib.use("TKAgg")
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from todloop.routines import Routine
from todloop.utils.pixels import PixelReader
from todloop.utils.cuts import pixels_affected_in_event

class FRB_Correlation_Filter(Routine):
    """A routine that checks for correlation between two signals"""
    def __init__(self, cosig_key, tod_key, output_key, coeff = 0.8):
        Routine.__init__(self)
        self._cosig_key = cosig_key
        self._tod_key = tod_key
        self._pr = None
        self._output_key = output_key
        self._coeff = coeff

    def initialize(self):
        self._pr = PixelReader()

    def execute(self):
        print '[INFO] Checking for correlation ...'
        tod_data = self.get_store().get(self._tod_key)  # retrieve tod_data
        cuts = self.get_store().get(self._cosig_key)  # retrieve tod_data
        peaks = cuts['peaks']
        #print('[INFO] peaks: ', peaks)
        
        def timeseries(pixel_id, s_time, e_time, buffer=10):

            start_time = s_time - buffer
            end_time = e_time + buffer

            a1, a2 = self._pr.get_f1(pixel_id)
            b1, b2 = self._pr.get_f2(pixel_id)
            d1, d2 = tod_data.data[a1], tod_data.data[a2]
            d3, d4 = tod_data.data[b1], tod_data.data[b2]

            # try to remove the mean from start_time to end_time
            d1 -= np.mean(d1[start_time:end_time])
            d2 -= np.mean(d2[start_time:end_time])
            d3 -= np.mean(d3[start_time:end_time])
            d4 -= np.mean(d4[start_time:end_time])
            
            time = tod_data.ctime - tod_data.ctime[0]
            time = time[start_time:end_time]
            
            d_1 = d1[start_time:end_time]
            d_2 = d2[start_time:end_time]
            d_3 = d3[start_time:end_time]
            d_4 = d4[start_time:end_time]

            return time, d_1

        def avg_signal(pixels,start_time,end_time):
           
            for pid in pixels:

                x = timeseries(pid,start_time,end_time)[0]
                y = timeseries(pid,start_time,end_time)[1]

                avg_y = np.zeros(len(y))

                avg_x = x
                avg_y += y

            x = avg_x
            y = avg_y/len(avg_y)
            return x, y

        def correlation(x1,x2,y1,y2):
            f1 = interp1d(x1,y1)
            f2 = interp1d(x2,y2)
            
            points = 100
            
            x1new = np.linspace( min(x1),max(x1),points)
            x2new = np.linspace( min(x2), max(x2), points)

            y1new = f1(x1new)
            y2new = f2(x2new)
            
            m_coeff = np.corrcoef(y1new,y2new)[0][1]

#            print '[INFO] Correlation matrix, coefficient: ', m_coeff 
            return m_coeff

            """
            plt.subplot(211)
            plt.plot( x1new,y1new,'g--')
            plt.title('Two Signals to Check for Correlation')
            plt.subplot(212)
            plt.plot(x2new,y2new,'r--')
            plt.xlabel('Cor. Matrix Coeff: ' + str(m_coeff))
            plt.show()
            """
            
        """
        CHECK CORRELATION BETWEEN SIGNALS FROM TWO EVENTS
        Find avgerage signal from an event, copy events from peaks data below
        To check correlation, call correlation function with event data
        """

        cs = cuts['coincident_signals']

        """
        FOR TWO SPECIFIC EVENTS
        """
        """
        event1 = [218306, 218449, 143, 37]
        stime1 = event1[0]
        etime1 = event1[1]
        pixels1 = pixels_affected_in_event(cs, event1)
        avg_x1, avg_y1 = avg_signal(pixels1, stime1, etime1)
        np.savetxt('slow_decay_template.txt',(avg_x1,avg_y1))

        
#        event2 = [205344, 205375, 31, 35]
        event2 = [9300,9303,3,2]
        stime2 = event2[0]
        etime2 = event2[1]
        pixels2 = pixels_affected_in_event(cs, event2)
        avg_x2, avg_y2 = avg_signal(pixels2, stime2, etime2)
        
        correlation(avg_x1,avg_x2, avg_y1, avg_y2)
        """

        """
        TEMPLATE FRB or CR  AS EVENT 1
        change name of .txt file to frb_template or cr_template 
        to check correlation for either signal 
        """
        data = np.genfromtxt('frb_template.txt')
        avg_x1, avg_y1 = data[0],data[1]

        """
        ALL EVENTS
        To compare all events in track to template, 
        initiate this loop
        """

        #Save outputs to a dictionary, here we initialize an empty dictionary
        tods = []
        lower_threshold = 0.6
        upper_threshold = self._coeff

        for event in peaks:
            all_pixels = pixels_affected_in_event(cs,event)
            avg_x2,avg_y2 = avg_signal(all_pixels,event[0],event[1])
            coeff = correlation(avg_x1,avg_x2, avg_y1, avg_y2)
       
            
            if lower_threshold <= coeff < upper_threshold:
                print '[INFO]: Possible FRB', event,'Coeff = ', coeff
            elif coeff >= upper_threshold:
                print '[INFO]: Highly Likely FRB', event, 'Coeff = ', coeff
                tod = {}
                tod['start'] = event[0]
                tod['end'] = event[1]
                tod['duration'] = event[2]
                tod['number_of_pixels'] = event[3]
                tod['pixels_affected'] = all_pixels
                tod['coefficient'] = coeff
                tods.append(tod)
    
            self.get_store().set(self._output_key, tods)

