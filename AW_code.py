def create_krig_grid(self, df, df_data='', spacing=500, top=''):
        """
        this will create and export/display a krig grid over the df points. it will auto generate a grid
        space over the area. 
        it will krig interpolate to fill the grid with values defined from df_data.
        outputs as a xyz csv or xyz format for kingdom import. 
        """
        # for testing purposes
        vari_types = ['linear', 'power', 'gaussian', 'spherical', 'exponential', 'hole-effect']
        vari_types = ['gaussian', 'spherical']
        nlags = [50,75,100, 150, 200, 300]
        yn=[True, False]
        yn=[True]

        df[df_data].dropna(inplace=True)
        df = df[['X', 'Y', df_data]]

        x= np.array(df['X']) 
        y= np.array(df['Y']) 
        z= np.array(df[df_data])

        x_min, x_max, y_min, y_max = [df.X.min()-spacing, df.X.max()+spacing, df.Y.min()-spacing, df.Y.max()+spacing]

        spacingx= int((x_max - x_min) // spacing) # calc number of bins to match spacing wanted. 
        spacingy= int((y_max - y_min) // spacing)

        grid_x = np.linspace(x_min, x_max, spacingx) # create grid spacin, with spacex bins
        grid_y = np.linspace(y_min, y_max, spacingy)

        vari_types = ['gaussian']
        nlags = [150]
        yn=[True]

        for vari in vari_types: # looop through all testing parameters  remove all loops if your set..
            for ans in yn:
                for nlagi in nlags:
                    OK = OrdinaryKriging(x, y, z, variogram_model=vari, enable_plotting=False, nlags=nlagi, exact_values=ans) # verbose=True,
                    z1, ss1 = OK.execute('grid', grid_x, grid_y)
                    xintrp, yintrp = np.meshgrid(grid_x, grid_y) 
                    fig, ax = plt.subplots(figsize=(30,30))

                    #ax.scatter(lons, lats, s=len(lons), label='Input data')
                    # boundarygeom = boundary.geometry

                    contour = plt.contourf(xintrp, yintrp, z1, len(z1), cmap=plt.cm.jet, alpha = 0.8) 
                    plt.colorbar(contour)
                    # boundary.plot(ax=ax, color='white', alpha = 0.2, linewidth=5.5, edgecolor='black', zorder = 5)
                    npts = len(x)
                    plt.scatter(x, y, marker='o', c='b', s=npts)
                    plt.xlim(x_min,x_max)
                    plt.ylim(y_min,y_max)
                    
                    plt.xticks(fontsize = 10, rotation=60)
                    plt.yticks(fontsize = 10)

                    plt.title(f'Spatial interpolation of {top},  {df_data} from {npts} wells.\n Using exact={ans}, {vari}, {nlagi} at {spacing}x{spacing}', fontsize = 18)
                    # plt.show()
                    plt.savefig(f'{top}-{vari}-{nlagi}-{ans}-{spacing}.png')

                    
                    ##  save the grid to a XYZ file..
                    # kt.write_zmap_grid(grid_x, grid_y, z1, 'outputd.zmap')
                    saveout=[]
                    for j in range(len(grid_x)):
                        for i in range(len(grid_y)):
                            saveout.append([grid_x[j], grid_y[i], z1.data[i][j]*-1])
                    griddf = pd.DataFrame(saveout, columns=['X', 'Y', df_data])

                    griddf.to_csv(f'{top}-{vari}-{nlagi}-{ans}-{spacing}.xyz', index=False, sep='\t')
        pass
